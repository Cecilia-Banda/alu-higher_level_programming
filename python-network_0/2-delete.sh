#!/bin/bash
#Script sending a DELETE request to the URL passed on first arguement and displays the body of the response
curl -sX DELETE "$1"
