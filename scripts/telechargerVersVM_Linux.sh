#!/bin/bash

# === CONFIGURATION ===
FILES_TO_SEND="ParDepartementDepuis2000.csv executer_depuis_vm.sh script.pig"
VM_USER="maria_dev"
VM_HOST="localhost"
VM_PORT=2222

# === TRANSFERT DES FICHIERS PRINCIPAUX ===
echo "Transfert des fichiers CSV, script Linux et script Pig vers la VM..."
scp -P $VM_PORT $FILES_TO_SEND $VM_USER@$VM_HOST:/home/$VM_USER/


# === INSTRUCTIONS POUR L'UTILISATEUR ===
echo
echo "Pour rendre ce script exécutable :"
echo "   chmod +x transfert_vers_vm.sh"
echo
echo "Pour l'exécuter :"
echo "   ./transfert_vers_vm.sh"

# === PAUSE POUR VOIR LE RÉSULTAT ===
echo
read -p "Appuyez sur Entrée pour quitter..."