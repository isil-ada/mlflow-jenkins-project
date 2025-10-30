import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pandas as pd
import sys

def train_model(n_estimators=100, max_depth=5):
    """
    Model eğitim fonksiyonu
    
    Args:
        n_estimators: Ağaç sayısı
        max_depth: Maksimum ağaç derinliği
    """
    
    # MLflow tracking sunucusu URL'i
    mlflow.set_tracking_uri("http://localhost:5000")
    
    # Deney (experiment) adı
    mlflow.set_experiment("iris_classification")
    
    # MLflow run başlat
    with mlflow.start_run():
        
        print("Veri yükleniyor...")
        # Veri yükleme
        iris = load_iris()
        X = pd.DataFrame(iris.data, columns=iris.feature_names)
        y = pd.Series(iris.target, name='target')
        
        # Veriyi eğitim ve test olarak böl
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"Model eğitiliyor... (n_estimators={n_estimators}, max_depth={max_depth})")
        
        # Model oluştur ve eğit
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X_train, y_train)
        
        # Tahminler yap
        y_pred = model.predict(X_test)
        
        # Metrikleri hesapla
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        
        # Parametreleri MLflow'a kaydet
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("test_size", 0.2)
        
        # Metrikleri MLflow'a kaydet
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        
        # Modeli MLflow'a kaydet
        mlflow.sklearn.log_model(model, "model")
        
        print("Model başarıyla MLflow'a kaydedildi!")
        
        # Model accuracy'si %85'in altındaysa hata ver (Jenkins için)
        if accuracy < 0.85:
            print(f"UYARI: Model accuracy ({accuracy:.4f}) çok düşük!")
            sys.exit(1)  # Jenkins'te build fail olacak
        
        return accuracy

if __name__ == "__main__":
    # Komut satırından parametreler al
    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    train_model(n_estimators, max_depth)