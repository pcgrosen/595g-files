# CS 595G at UCSB

Welcome to 595g! This repo will help guide you through various important aspects
of your server.

## Introduction

These servers are in place to facilitate a consistent environment for use in
solving challenges. As such, challenges will be distributed through the server
infrastructure. You can find currently live challenges in `/opt/challenges/`.

During initial testing, you will likely want to attack the service running on
your local box in order to get the best view of the outcome (e.g. using gdb).
However, **in your final solution scripts, you will need to modify your scripts
to attack the vuln server.** The vuln server is located at `10.0.10.10`.

You will also submit your solutions via your server. To submit a solution, place
your solution script in the directory at`/opt/solutions/<challenge name>/` where
the name is the same as in the challenges directory. Don't worry your solution
being in any particular format -- I will read your code and figure it out
myself. (Obviously, follow good programming practices and make it readable ...)

In order to provide the most real-world environment possible, you have root
access on your server. You can run commands as root using `sudo`. No password is
required when doing this as the `ubuntu` user. Be careful. Consider what you are
doing before executing commands as root.

## Restrictions

There are several restrictions in place on your servers to protect their
integrity:

1. No inbound traffic is allowed on ports 5000-5999 ("challenge ports")

2. Inbound public traffic is only allowed on port 22 (ssh)

The vuln server is slightly different:

1. Vuln servers can only be attacked from inside the cloud network (i.e. only
from your server).

## Rules

**These servers are provided for your benefit. Do not abuse this privilege.**

1. Do not attack infrastructure that is not part of a challenge.

2. Do not attack other students, except where explicitly allowed.

3. Follow all UCSB computer use policy.

4. Do not remove my key (labeled `manager`) from your authorized keys.

5. Do not shut down your server (restarting is fine).

6. These servers are not for private use. Do not store sensitive data on them.

7. Do not perform non-class related activites on these servers.

If you accidentally violate one of these rules, please let me know as soon as
possible, and I'll work with you to fix it.

**If I find you in intentional or severe violation of these rules, I reserve the
right to terminate or disconnect your server.**
