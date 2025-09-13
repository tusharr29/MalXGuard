# 🛡️ MalXGuard: Malware Classification System  

MalXGuard is a machine learning-based malware detection and classification system.  
It extracts features from raw `.asm` and `.bytes` files, applies NLP-based techniques, and classifies malware into multiple families using machine learning models.  

Blog: https://kiiocity.wordpress.com/2022/05/08/anomaly-based-malware-detection-1/

With the rapid development of the Internet, malware became one of the major cyber threats nowadays. Any software performing malicious actions, including information stealing, espionage, etc. can be referred to as malware. Kaspersky Labs (2017) define malware as “a type of computer program designed to infect a legitimate user's computer and inflict harm on it in multiple ways.”.

While the diversity of malware is increasing, anti-virus scanners cannot fulfil the needs of protection, resulting in millions of hosts being attacked. According to Kaspersky Labs (2016), 6,563,145 different hosts were attacked, and 4,000,000 unique malware objects were detected in 2015. In turn, Juniper Research (2016) predicts the cost of data breaches to increase to $2.1 trillion globally by 2019.

In addition to that, there is a decrease in the skill level that is required for malware development, due to the high availability of attacking tools on the Internet nowadays. High availability of anti-detection techniques, as well as ability to buy malware on the black-market result in the opportunity to become an attacker for anyone, not depending on the skill level. Current studies show that more and more attacks are being issued by script-kiddies or are automated. (Aliyev 2010).

Malware detection through standard, signature-based methods is getting increasingly difﬁcult since all current malware applications tend to have multiple polymorphic layers to avoid detection or to use side mechanisms to automatically update themselves to a newer version at short periods of time to avoid detection by any antivirus software.

Machine learning helps antivirus software detect new threats without relying on signatures. In the past, antivirus software relied largely on fingerprinting, which works by cross-referencing files against a huge database of known malware.
---

## Objective

As stated before, Malware detectors that are based on signatures can perform well on previously-known malware, that was already discovered by some anti-virus vendors. However, it is unable to detect polymorphic malware, that has the ability to change its signatures, as well as new malware, for which signatures have not been created yet. In turn, the accuracy of heuristics-based detectors is not always sufficient for adequate detection, resulting in a lot of false positives and false negatives. (Baskaran and Ralescu 2016). The need for the new detection methods is dictated by the high spreading rate of polymorphic viruses.

## Existing Model

Although not widely implemented, the concept of machine learning methods for malware detection is not new. Several types of studies were carried out in this field, aiming to figure the accuracy of different methods.

In his paper “Malware Detection Using Machine Learning” Dragos Gavrilut aimed for developing a detection system based on several modified perceptron algorithms. For different algorithms, he achieved the accuracy of 69.90%- 96.18%. It should be stated that the algorithms that resulted in best accuracy also produced the highest number of false-positives: the most accurate one resulted in 48 false positives. The most balanced algorithm with appropriate accuracy and the low false-positive rate had the accuracy of 93.01%. (Gavrilut,et al. 2009)

“A Static Malware Detection System Using Data Mining Methods” proposed extraction methods based on PE headers, DLLs and API functions and methods based on Naive Bayes, J48 Decision Trees, and Support Vector Machines. Highest overall accuracy was achieved with the J48 algorithm (99% with PE header feature type and hybrid PE header & API function feature type, 99.1% with API function feature type). (Baldangombo, Jambaljav and Horng 2013)

## 📌 Project Overview  
- Detects and classifies malware into families.  
- Uses **TF-IDF feature extraction** on assembly and bytecode files.  
- Trains a **Random Forest classifier** (extendable to other ML models).  
- Includes an **inference API** for predictions on new samples.  

---

## ⚙️ Features  
✅ Extracts features from `.asm` and `.bytes` malware files  
✅ Converts raw data into vectorized representations (TF-IDF)  
✅ Trains machine learning models for classification  
✅ Provides inference script for real-time predictions  
✅ Modular structure for easy extension  

---

## Future Enhancement

Use a wider, well-labelled dataset.
Instead of only hosting it in our local system, we can upload it in the web and provide the feature of uploading files to be checked and also create a section for URL detector.
GUI based program can be made for windows, as of now it is only made for terminal.
Real time scanning of every file while downloading/transferring can be done to be used in daily life scenario to detect malicious files.

## Some Interesting facts about Malwares

Trojan is a malware which masks as another software. Trojan is from the infamous Greek Trojan Horse used to infiltrate and defeat Troy. Like virus and worms, Trojan is equally destructive which displaying annoying pop ups, and opens backdoor for other malware to access to. Yet, worms and (some) virus replicates but not Trojan. When Trojan infects other devices, it becomes a virus.

## 🚀 Installation  

```bash
# Clone the repository
git clone https://github.com/tusharr29/MalXGuard.git
cd MalXGuard

# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt


