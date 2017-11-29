# Project Walkthrough

# Prerequisites

In the machine tested, I used the built in wireless adapter and connected to internet through Ethernet

# System Setup

## Install mitmproxy

Get instruction from [their site](www.mitmproxy.org)

## Setup ip forwarding

The below commands assumes you're running as root:

    sysctl -w net.ipv4.ip_forward=1

## Setup routing using IPtables

As for my machine, my wireless adapter is named `wlp3s0`. Make sure that the port you will be using for `mitmproxy` matches the `--dport` option (destination port). Again, root privileges required

    iptables -t nat -A PREROUTING -i wlp3s0 -p tcp --dport 80 -J REDIRECT --to-port 8080

# Executing Man in the middle attack

## Real execution

    mitmdump -T -p 8080 -i -s "inject.py test.js" "~t 'text/html' ~s ~c 200"

`mitmdump` does what `mitmproxy` but in an automated way. `mitmproxy` allows interception but manually, hence, Testing section is for learning.

## Testing (optional, if you want to know whats happening)

Run `mitmproxy -T -p 8080` . The port should match the `iptables` destination port.

Try a site like [httpbin.org](http://www.httpbin.org). You should now be able to see traffic in the screen. Press `?` for instructions.

To intercept, press `i`. Set the following filters:

   Intercept filter: ~t "text/html" ~s ~c 200 
    
