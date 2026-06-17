# Q-SHIELD
Q-SHIELD: A Hybrid Post-Quantum Cybersecurity Framework for Secure Communication
# Q-SHIELD

## Q-SHIELD: A Hybrid Post-Quantum Cybersecurity Framework for Secure Communication

This repository contains the implementation, experimental scripts, datasets, and evaluation results of the **Q-SHIELD** framework, a hybrid post-quantum cybersecurity architecture designed to provide secure and efficient communication in the presence of classical and quantum adversaries.

The following publicly available datasets were used in this work:

UNSW-NB15
CIC-IDS2017
MAWI Traffic Archive

Due to licensing and storage limitations, the datasets are not redistributed in this repository. Users may download them from their official sources and place them in the datasets/ directory before running the experiments.

---

## Abstract

Q-SHIELD is a performance-oriented hybrid post-quantum cybersecurity framework that integrates the Kyber-768 Key Encapsulation Mechanism (KEM) with Authenticated Encryption with Associated Data (AEAD) and a session-aware optimization mechanism. The framework provides post-quantum security while improving system efficiency by reducing redundant key establishment operations. Experimental results demonstrate reductions in session setup latency and energy consumption compared with standalone lattice-based approaches while maintaining equivalent post-quantum security guarantees.

---

## Features

* Post-Quantum Key Encapsulation using **Kyber-768**
* Authenticated Encryption with Associated Data (**AEAD**)
* Session-aware optimization mechanism
* Protection against:

  * Man-in-the-Middle (MITM) attacks
  * Replay attacks
  * Ciphertext tampering attacks
* Performance benchmarking
* Communication overhead analysis
* Energy consumption analysis
* Scalability evaluation
* Statistical significance analysis

---

## Repository Structure

```text
Q-SHIELD/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── qshield_framework.py
│   ├── kyber_module.py
│   ├── aead_module.py
│   ├── session_manager.py
│   └── attack_simulation.py
│
├── experiments/
│   ├── performance_benchmark.py
│   ├── communication_overhead.py
│   ├── energy_estimation.py
│   ├── scalability_test.py
│   └── statistical_analysis.py
│
├── datasets/
│   ├── traffic_data.csv
│   └── replay_attack_trace.csv
│
├── results/
│   ├── Table4_results.csv
│   ├── Table5_results.csv
│   ├── Table6_results.csv
│   └── figures/
│
└── docs/
    └── experimental_setup.md
```

---

## Requirements

* Python 3.10 or higher
* NumPy
* Pandas
* SciPy
* Matplotlib
* Cryptography
* liboqs
* oqs-python

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Framework

Execute the main framework:

```bash
python src/qshield_framework.py
```

Run performance evaluation:

```bash
python experiments/performance_benchmark.py
```

Run scalability analysis:

```bash
python experiments/scalability_test.py
```

Run energy estimation:

```bash
python experiments/energy_estimation.py
```

Run attack simulations:

```bash
python src/attack_simulation.py
```

---

## Experimental Results

The repository includes:

* Key establishment performance comparison
* Communication overhead analysis
* Energy consumption analysis
* Security evaluation against representative attacks
* Scalability analysis
* Statistical significance analysis

All experiments were conducted under identical hardware and software configurations and repeated 50 times to ensure reproducibility.

---

## Security Properties

The Q-SHIELD framework provides:

* IND-CCA secure post-quantum key establishment
* Forward secrecy
* Authentication and integrity
* Resistance against:

  * Shor's algorithm
  * Grover's algorithm
  * MITM attacks
  * Replay attacks
  * Ciphertext tampering

---

## Citation

If you use this repository in your research, please cite:

Dhaya R, *Q-SHIELD: A Hybrid Post-Quantum Cybersecurity Framework for Secure Communication*, 

---

## License

This project is released under the **MIT License**.
