QuickNotes: Cloud-Native Not Uygulaması
Bu proje, Google Kubernetes Engine (GKE) üzerinde çalışan, yüksek erişilebilirliğe ve güvenliğe sahip bir not alma uygulamasıdır.

1. Uygulama ve Sistem Mimarisi
Uygulama, Python (Flask) tabanlı olup MySQL veritabanı ile etkileşim kurar.

Uygulama Mimarisi: İnce ve hafif bir Docker imajı (python:3.10-slim) üzerine kurulmuştur.

Sistem Mimarisi: GKE üzerinde çalışan, harici trafiği LoadBalancer ile karşılayan ve veritabanını izole eden bir yapıdır.

2. Kubernetes Mimarisi (k8s/)
Projemiz "Infrastructure as Code" (IaC) ilkeleriyle modüler hale getirilmiştir:

deployment.yaml: Uygulama ve veritabanı konteynerlerinin çalışma durumunu yönetir.

service.yaml: Dahili (ClusterIP) ve harici (LoadBalancer) ağ trafiğini yönlendirir.

pvc.yaml: Veri kalıcılığı için 1GB Persistent Volume Claim (Veritabanı verilerini korur).

network-policy.yaml: MySQL veritabanına sadece quicknotes uygulamasının erişebilmesini sağlayarak "Zero Trust" güvenliğini uygular.

3. CI/CD Pipeline Akışı
cloudbuild.yaml dosyası ile tam otomasyon süreci:

Push: Kodlar GitHub'a gönderilir.

Build & Push: Cloud Build yeni Docker imajını derler ve Google Container Registry'ye (GCR) gönderir.

Deploy: Pipeline otomatik olarak GKE üzerindeki imajı kubectl set image komutuyla günceller (Rolling Update).

4. Yönetim ve Test Komutları
Sunum sırasında sistemi yönetmek için kullanacağın komutlar:

Ölçekleme (Scaling): kubectl scale deployment quicknotes-deployment --replicas=3

Sistem Durumu: kubectl get pods

Geri Dönüş (Rollback): kubectl rollout undo deployment quicknotes-deployment

Yeniden Başlatma: kubectl rollout restart deployment quicknotes-deployment
