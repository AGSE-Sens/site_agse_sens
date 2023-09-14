#!/bin/bash
password=''
echo -n "Choisir le mot de passe : "
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
python3 -m venv env
. env/bin/activate
python3 -m pip install --upgrade -r requirement.txt
python3 -m pip cache purge
echo "import os;open('key.txt','wb').write((os.urandom(40)))" | python3 && \
echo "La clée de sécurité à été générée."
echo "from werkzeug.security import generate_password_hash;open('hash.txt','w').write((generate_password_hash('"$password"')))" | python3 && \
echo "Le mot de passe des pages privées a été enregistré."
git submodule update --remote --depth 1
echo -e "#!/bin/bash
. env/bin/activate
export FLASK_DEBUG=ON
flask run
deactivate" > run.sh && chmod +x run.sh
echo -e "#!/bin/bash
. env/bin/activate
python3 freeze.py
deactivate" > freeze && chmod +x freeze
#~ ./freeze
deactivate
