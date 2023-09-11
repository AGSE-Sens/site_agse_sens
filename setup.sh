#!/bin/bash
rm -fr env
python3 -m venv env
. env/bin/activate
python3 -m pip install --upgrade -r requirement.txt
python3 -m pip cache purge
echo "import os;open('key.txt','wb').write((os.urandom(40)))" | python3 && \
echo "La clée de sécurité à été générée."
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
