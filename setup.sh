#!/bin/bash
password=''
echo -n "Mot de passe Admin :"
while IFS= read -r -s -n1 char; do
  [[ -z $char ]] && { printf '\n' >/dev/tty; break; } # ENTER pressed; output \n and break.
  if [[ $char == $'\x7f' ]]; then # backspace was pressed
      # Remove last char from output variable.
      [[ -n $password ]] && password=${password%?}
      # Erase '*' to the left.
      printf '\b \b' >/dev/tty
  else
    # Add typed char to output variable.
    password+=$char
    # Print '*' in its stead.
    printf '*' >/dev/tty
  fi
done
rm -fr env
python -m venv env
. env/bin/activate
pip install -r requirement.txt
pip cache purge
echo -n "from werkzeug.security import generate_password_hash;print(generate_password_hash('"$password"'))" | python > admin.txt && \
echo "Le mot de passe Administrateur du site a été enregistré."
echo -n "import os;print(os.urandom(40))" | python > key.txt && \
echo "La clée de sécurité à été générée."
cd application
rm -fr src
git clone --depth=1 https://github.com/AGSE-Sens/src
cd ..
