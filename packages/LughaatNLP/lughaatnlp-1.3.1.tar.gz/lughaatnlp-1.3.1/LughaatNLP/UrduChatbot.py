import torch
import torch.nn as nn
import pandas as pd
from transformers import DistilBertTokenizer, DistilBertModel
from torch.utils.data import DataLoader, TensorDataset, RandomSampler
from tqdm import tqdm
import os
import warnings
import logging
warnings.filterwarnings('ignore')


class UrduChatbotModel(nn.Module):
    def __init__(self, num_labels, dropout_rate=0.1):
        super(UrduChatbotModel, self).__init__()
        self.distilbert = DistilBertModel.from_pretrained('muhammadnoman76/LughaatBERT')
        self.dropout = nn.Dropout(dropout_rate)
        self.classifier = nn.Linear(768, num_labels)
        
    def forward(self, input_ids, attention_mask):
        outputs = self.distilbert(input_ids, attention_mask=attention_mask)
        cls_output = outputs[0][:, 0]
        dropout_output = self.dropout(cls_output)
        return self.classifier(dropout_output)

class UrduChatbot:
    def __init__(self, max_length=55, batch_size=32, learning_rate=2e-5):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = DistilBertTokenizer.from_pretrained('muhammadnoman76/LughaatBERT')
        self.max_length = max_length
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.model = None
        self.answers = None
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = None

    @staticmethod
    def calculate_metrics(predictions, labels):
        """Calculate overall accuracy, F1 score, and precision"""
        unique_labels = list(set(labels + predictions))
        num_classes = len(unique_labels)
        correct = sum(predictions[i] == labels[i] for i in range(len(predictions)))
        accuracy = correct / len(predictions) if len(predictions) > 0 else 0

        tp = fp = fn = 0
        for i in range(len(predictions)):
            if predictions[i] == labels[i]:
                tp += 1
            else:
                fp += 1
                fn += 1  

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0

        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        return {
            'accuracy': round(accuracy, 3),
            'f1_score': round(f1_score, 3),
            'precision': round(precision, 3)
        }

    def prepare_data(self, csv_path):
        df = pd.read_csv(csv_path)
        columns = df.columns[:2]
        questions = df[columns[0]].tolist()
        
        current_answers = df[columns[1]].unique().tolist()
        old_num_labels = len(self.answers) if self.answers is not None else 0
        
        if self.answers is None:
            self.answers = current_answers
        else:
            new_answers = [ans for ans in current_answers if ans not in self.answers]
            if new_answers:
                self.answers.extend(new_answers)
                if self.model is not None:
                    new_classifier = nn.Linear(768, len(self.answers)).to(self.device)
                    with torch.no_grad():
                        new_classifier.weight[:old_num_labels] = self.model.classifier.weight
                        new_classifier.bias[:old_num_labels] = self.model.classifier.bias
                    self.model.classifier = new_classifier
                    self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.learning_rate)

        encodings = self.tokenizer(
            questions,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
      
        labels = [self.answers.index(ans) for ans in df[columns[1]]]
        labels = torch.tensor(labels)
    
        dataset = TensorDataset(
            encodings['input_ids'],
            encodings['attention_mask'],
            labels
        )
        
        return dataset
    
    def initialize_model(self, num_labels=None):
        if num_labels is None and self.answers is not None:
            num_labels = len(self.answers)
        elif num_labels is None:
            raise ValueError("Either num_labels must be provided or prepare_data must be called first")
            
        self.model = UrduChatbotModel(num_labels)
        self.model.to(self.device)
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.learning_rate)
    
    def train(self, dataset, epochs=3, continue_training=False):
        if self.model is None:
            self.initialize_model()
            
        if not continue_training:
            self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.learning_rate)
        
        dataloader = DataLoader(
            dataset,
            batch_size=self.batch_size,
            sampler=RandomSampler(dataset)
        )
        
        for epoch in range(epochs):
            print(f'\nEpoch {epoch + 1}/{epochs}')
            self.model.train()
            total_loss = 0
            
            for batch in tqdm(dataloader, desc="Training"):
                input_ids, attention_mask, labels = [b.to(self.device) for b in batch]
                
                self.optimizer.zero_grad()
                outputs = self.model(input_ids, attention_mask)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                
                total_loss += loss.item()
            
            avg_loss = total_loss / len(dataloader)
            print(f'Average Loss: {avg_loss:.4f}')
    
    def save_model(self, path):
        directory = os.path.dirname(path)
        if directory != '':
            os.makedirs(directory, exist_ok=True)
        
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'answers': self.answers,
            'optimizer_state_dict': self.optimizer.state_dict() if self.optimizer else None
        }, path)
    
    def load_model(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"No model file found at {path}")
            
        checkpoint = torch.load(path)
        self.answers = checkpoint['answers']
        self.initialize_model(len(self.answers))
        self.model.load_state_dict(checkpoint['model_state_dict'])
        
        if checkpoint['optimizer_state_dict'] is not None:
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
            
        self.model.eval()
    
    def predict(self, question, confidence_threshold=0.0):
        if self.model is None:
            raise ValueError("Model must be loaded or trained before making predictions")

        self.model.eval()
        encoding = self.tokenizer(
            question,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        input_ids = encoding['input_ids'].to(self.device)
        attention_mask = encoding['attention_mask'].to(self.device)

        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, prediction = torch.max(probabilities, dim=1)
            confidence = confidence.item()

            if confidence >= confidence_threshold:
                return self.answers[prediction.item()], confidence
            else:
                return None, confidence

    def evaluate(self, csv_path):
        """
        Evaluate model directly from a CSV file
        """
        # Prepare the test dataset from CSV
        test_dataset = self.prepare_data(csv_path)

        dataloader = DataLoader(test_dataset, batch_size=self.batch_size)
        self.model.eval()

        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch in dataloader:
                input_ids, attention_mask, labels = [b.to(self.device) for b in batch]
                outputs = self.model(input_ids, attention_mask)
                preds = torch.argmax(outputs, dim=1)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())

        all_preds = [self.answers[pred] for pred in all_preds]
        all_labels = [self.answers[label] for label in all_labels]

        return self.calculate_metrics(all_preds, all_labels)