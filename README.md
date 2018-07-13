# JPEO JTRS Standard APIs REDHAWK IDL Projects

## Description

Those Projects are based on JTNC Standard API Documents found in [www.public.navy.mil](http://www.public.navy.mil/jtnc/Pages/resources.aspx?filter=cat-api), minor changes are made in order to adapt the IDLs to the REDHAWK Target SDR IDL Repository.

## Installation Instructions

You just need to to run:

	$ ./install

at the top level directory. It will generate the required source files, build and install the Interfaces libraries into $OSSIEHOME. Use `./install -m <module_name>` to install a specific JTNC CORBA Module. Use `./install -f` to reinstall JTNC CORBA Module(s).
Note: sudo privileges are required
