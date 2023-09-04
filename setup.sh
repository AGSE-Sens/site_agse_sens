#!/bin/bash
rm -fr env
python3 -m venv env
. env/bin/activate
python3 -m pip install --upgrade -r requirement.txt
python3 -m pip cache purge
git submodule update --remote --merge
echo "#!/bin/bash \
. env/bin/activate \
export FLASK_DEBUG=ON \
flask run \
deactivate" > run.sh && chmod +x run.sh
