import pdfplumber
import requests, PyPDF2, io
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pdfplumber
from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
from tabulate import tabulate
import os


file = open("tabela.txt", "w")


artigos = ['A comprehensive semantic-based resource allocation framework for workflow management systems.pdf', 'A framework for modeling and reasoning about network management resources and services to support information reuse.pdf', 'A multi-layered agent ontology system for resource inventory.pdf', 'A semantic approach to evaluate the impact of cyber actions on the physical domain.pdf',
           'A semantic model for enhancing network services management and auditing.pdf', 'A study in the expressiveness of semantically different policy modelling schemes.pdf', 'An ontology-based approach for semantic interoperability in interorganizational IT service management.pdf', 'An ontology-based approach to the description and execution of composite network management processes for network monitoring.pdf',
           'An Ontology-Based Information Extraction System for bridging the configuration gap in hybrid SDN environments.pdf', 'Application of OWL-S to define management interfaces based on Web services.pdf', 'Composing user network operation services using Web service composition techniques.pdf',
           'Enhancing Event Processing Networks with semantics to enable self-managed SEE federations.pdf', 'ENM_ A service oriented architecture for ontology-driven network management in heterogeneous network infrastructures.pdf', 'Implementation and application of a well-founded configuration management ontology.pdf', 'Integrating heterogeneous IT_network management models using linked data.pdf',
           'Multi-domain fault management architecture based on a Shared ontology-based Knowledge Plane.pdf', 'Network access control configuration management using semantic web techniques.pdf', 'New developments in ontology-based policy management- Increasing the practicality and comprehensiveness of KAoS.pdf', 'Ontological configuration management for wireless mesh routers.pdf',
           'Ontological semantics for distributing contextual knowledge in highly distributed autonomic systems.pdf', 'Ontology-based information extraction from the configuration command line of network routers.pdf', 'Ontology-based policy refinement using SWRL rules for management information definitions in OWL.pdf', 'Ontology-based policy translation.pdf', 'Ontology-driven automatic construction of bayesian networks for telecommunication network management.pdf',
           'Resolving tactical network management interoperability by using ontology.pdf', 'Semantic context dissemination and service matchmaking in future network management.pdf', 'Semantic matching of security policies to support security experts.pdf', 'SINMS- A slow intelligence network manager based on SNMP protocol.pdf', 'The STAC (security toolbox- Attacks _ countermeasures) ontology.pdf',
           'Towards an information model that supports service-aware, self-managing virtual resources.pdf', 'Towards automation for pervasive network security management using an integration of ontology-based and policy-based approaches.pdf']


# ARTIGO QUE GERA ERROR: 'Similarity and logic based ontology mapping for security management.pdf'



termos = ["RDF", "Protege", "OWL", "ITU", "ISO","TMFORUM", "DMTF", "IETF", "F-LOGIC", "RDFS", "CIM", "Accounting", "fault", "performance", "Security", "configuration"]

data = {}
dado = {}
totalPDF = []
soma = {'RDF':0, 'Protege':0, 'OWL':0, 'ITU':0, 'ISO':0,'TMFORUM':0, 'DMTF':0, 'IETF':0, 'F-LOGIC':0, 'RDFS':0, 'CIM':0, 'Accounting':0, 'fault':0, 'performance':0, 'Security':0, 'configuration':0}


for artigo in artigos:


    pdf = pdfplumber.open(f'artigos/{artigo}')
    cont = 0
    occurrences = 0


    for palavra in termos:
        with open((f'artigos/{artigo}'), "rb") as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            numpaginas = pdf_reader.numPages

            for i in range(0, numpaginas):
                page = pdf.pages[i]
                text = page.extract_text()

                # Contando as palavras por página
                tokens = word_tokenize(text)
                punctuation = ['(', ')', ';', ':', '[', ']', ',']
                stop_words = stopwords.words('english')
                keywords = [Word for Word in tokens if not Word in stop_words and not Word in punctuation]
                for k in keywords:
                    if palavra == k: occurrences += 1
                dado[palavra] = occurrences

    print("funcionando")
    data[artigo] = dado
    dado = {}


# Escreve os dados de cada artigo e as respectivas vezes que uma palavra aparece e armazena em um arquivo .txt
for chave in data.keys():
  print(f'\n\n ARTIGO: {chave}')
  file.write(f'ARTIGO: {chave}\n')
  for key, value in data[chave].items():
    print(f'{key}:{value} | ', end="")
    file.write(f'{key}:{value} | ')

    #Somando todos termos
    soma[key] = soma[key] + value


  file.write(f'\n\n')

#Fechando arquivo
file.close()



# Criando gráfico de pizza
plt.pie([float(soma[v]) for v in soma], labels=[str(k) for k in soma], autopct='%1.1f%%')
plt.show()
