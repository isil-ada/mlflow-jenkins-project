---

# MLflow-Jenkins MLOps Projesi

Bu proje, **üniversite dersi kapsamında** gerçekleştirilmiş bir **MLOps uygulama çalışmasıdır**.
Amaç, **MLflow** ile makine öğrenimi deneylerinin yönetimini ve **Jenkins** ile sürekli entegrasyon / sürekli teslimat (CI/CD) süreçlerini uygulamalı olarak öğrenmek ve göstermekti.

Proje, akademik amaçlarla hazırlanmış olup **eğitim odaklı bir örnek çalışma** niteliğindedir.

---

## Ders Kapsamı

Bu çalışma kapsamında aşağıdaki kavramlar uygulamalı olarak ele alınmıştır:

* Makine öğrenimi deney takibi (MLflow)
* Model eğitimi ve değerlendirme süreçleri
* Deney sonuçlarının ve artefaktların kaydedilmesi
* Jenkins ile CI/CD pipeline oluşturma
* MLOps temel prensiplerinin anlaşılması

---

## Proje Fikir Özeti

Bu projede:

* **MLflow** kullanılarak makine öğrenimi deneyleri izlenmiş, metrikler ve modeller kaydedilmiştir.
* **Jenkins** aracılığıyla model eğitim süreci otomatikleştirilmiş ve CI/CD mantığı uygulanmıştır.
* Model geliştirme sürecinin tekrar edilebilir ve izlenebilir olması hedeflenmiştir.

Bu yapı, **MLOps yaklaşımının akademik düzeyde anlaşılması** için örnek bir senaryo sunar.

---

## Proje Yapısı

```
mlflow-jenkins-project/
├── mlartifacts/            # MLflow artifact çıktıları
├── mlruns/                 # MLflow deney kayıtları
├── src/                    # Model eğitim ve deney kodları
├── Jenkinsfile             # Jenkins pipeline tanımı
├── requirements.txt        # Python bağımlılıkları
├── README.md               # Proje açıklaması
```

---

## Kurulum ve Çalıştırma

### Gereksinimler

* Python 3.x
* MLflow
* Jenkins (Pipeline desteği açık)

Bağımlılıkların kurulumu:

```bash
pip install -r requirements.txt
```

---

## MLflow Kullanımı

MLflow, bu projede deneylerin izlenmesi ve model çıktılarının saklanması için kullanılmıştır.

```bash
mlflow run .
```

Bu komut ile deney çalıştırılır ve sonuçlar **mlruns/** dizini altında kaydedilir.

---

## Jenkins CI/CD Pipeline

Proje kök dizininde bulunan **Jenkinsfile**, ders kapsamında CI/CD mantığını göstermek amacıyla hazırlanmıştır.

Pipeline şu adımları içerir:

1. Projenin GitHub’dan çekilmesi
2. Python ortamının hazırlanması
3. MLflow deneylerinin çalıştırılması
4. Sonuçların loglanması

Bu yapı, **model geliştirme sürecinin otomatikleştirilmesini** göstermeyi amaçlar.

---

## Not

> Bu proje **akademik ve eğitim amaçlıdır**.
> Gerçek üretim ortamları için ek güvenlik, ölçeklenebilirlik ve izleme mekanizmaları gerektirir.

---

## 👩‍🎓 Katkı ve Kullanım

Bu proje ders kapsamında bireysel bir çalışma olarak hazırlanmıştır.
Eğitim amaçlı inceleme ve geliştirmelere açıktır.

---
