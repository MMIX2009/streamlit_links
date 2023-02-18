import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('azure.png', width=200))

st.header('Azure Kubernetes Services (AKS)')

st.info('AKS Kubenets, CNI, CNI overlay')

icon_size = 20

st_button('youtube', 'https://learn.microsoft.com/en-us/azure/aks/concepts-network#kubenet-basic-networking', 'AKS Concepts', icon_size)
st_button('youtube', 'https://learn.microsoft.com/en-us/azure/aks/configure-kubenet', 'AKS Kubenet', icon_size)
st_button('medium', 'https://inder-devops.medium.com/aks-networking-deep-dive-kubenet-vs-azure-cni-vs-azure-cni-overlay-a51709171ce9', 'AKS Networking Deep Dive', icon_size)
st_button('twitter', 'https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni', 'AKS CNI model', icon_size)
st_button('linkedin', 'https://learn.microsoft.com/en-us/azure/aks/azure-cni-overlay', 'AKS CNI Overlay model', icon_size)
st_button('newsletter', 'https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-network', 'AKS Operator Best Practices', icon_size)
st_button('cup', 'https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium', 'Azure CNI powered by Cilium', icon_size)
st_button('youtube', 'https://learn.microsoft.com/en-us/azure/aks/configure-kubenet-dual-stack?tabs=azure-cli%2Ckubectl', 'AKS Kubenet dual stack', icon_size)
st_button('youtube', 'https://learn.microsoft.com/en-us/azure/aks/use-byo-cni?tabs=azure-cli', 'AKS BYO CNI', icon_size)
st_button('youtube', 'https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni-dynamic-ip-allocation', 'AKS CNI Dynamic IP configuration', icon_size)
