#!/bin/sh

pkg install curl

# To install particular version/variant of software
pkg search PKGNAME

#This will show all available packages
pkg install PKGNAME_VARIANT

#To see all the installed packages
pkg info

#Remove package from the system
pkg delete perl

#Upgrade all the packages in pkgng database
pkg upgrade 

#Check packages for known vunerabilities
pkg audir -F

#Automatically remove Leftovers
pkg autoremove

#To backup Package database
pkg backup -d DBNAME.db

#To reinstall package
pkg install -Rf PKGNAME
