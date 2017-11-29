real() {
    mitmdump -T -p 8080 -s "injectJS.py test.js" "~t 'text/html' ~s ~c 200"
}

testing() {
    mitmproxy -T -p 8080 -i "~t 'text/html' ~s ~c 200" -s "injectJS.py test.js"
}

$@
