DIR=/Users/MDRAHALI/Desktop/Learning_Roadmap/Mastring_FLASK_Web_Development/Flask_Youtube_Video_Embbed_GZIP_Compressing_Extensions/Flask-YouTube
pushd $DIR
pip uninstall flask-youtube
python setup.py build
python setup.py install
popd

