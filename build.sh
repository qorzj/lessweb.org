mkdir -p static/__javascript__
rm -rf lessweb_org/view/__javascript__/* static/__javascript__/*

PYTHONPATH=".:$PYTHONPATH" transcrypt -b -a -k -n -e 6 smscaptcha/view/design.py && \
PYTHONPATH=".:$PYTHONPATH" transcrypt -b -a -k -n -e 6 smscaptcha/view/homepage.py && \

mv lessweb_org/view/__javascript__/* static/__javascript__/