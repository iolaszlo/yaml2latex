# yaml2latex
(YAML AND TEX TEMPLATES) to TEX GENERATOR   
==========================================
### Introduction:

This is another YAML to LATEX, Curriculum Vitae generator with an extension to general purpose yaml2latex projects in mind.

1.What does it do? Input:(YAML+latex templates) -->Output: self contained tex file ready for compilation into pdf.

2.How to use it? 


       a)For users:
   	 Modify the yaml file in the "example" directory to your own liking, then run "runme.sh" to generate your
 self contained "cv.tex".


       b)For developers:
	 Modify the yaml/tex templates and the code nin "mkresume.py" to meet your own templating needs. 
With small modifications in this simple code a more general yaml to tex generation toolchain can be set up.


### Acknowledgements:
This project is inspired by the work of:
 Aleksandr Mattal <a href="https://github.com/QuteBits/resume_42">https://github.com/QuteBits/resume_42"</a> and 
 by the work of Brandon Amos: <a href="https://github.com/bamos/cv">https://github.com/bamos/cv</a>



### Pre-Install:


Dependencies:a) A linux distro with "bash" working


	     b)	A modern version of Python, with the dependencies listed in "mkresume.py" installed
	     
### Install:

1.)Download and extract this whole project from GitHub.


2.)Make the files "mkresume.py" and  "runme.sh" executable if necessary.

### Use:
 
Option a.) View and run the "runme.sh" file for a working example. The output will be in "example/cv.tex"


Option b.) Run "mkresume.py" -h for info on the input and output


        In short you have to give as input: 
	  -1.) YAML FILE, consistent with the script                  (see example/resume.yaml)

	  -2.) PATH TO TEMPLATES, path where your template .tex files are located (see example/template)

          -3.) HEADER TEMPLATE, name of HEADER template file (see example/template/cvhead1.tex

          -4.) BODY TEMPLATE, name of BODY template file (see example/template/cvbody1.tex)


### Contact:
 laszlo.g.papp@gmail.com


### License:

This work is distributed under the MIT license (`LICENSE-lacippp3.mit`) with portions copyright Aleksandr Mattal from [QuteBits/resume_42](https://github.com/QuteBits/resume_42) Ellis Michael from [emichael/resume](https://github.com/emichael/resume) and Brandon Amos from [bamos/cv](https://github.com/bamos/cv). Their portions are also distributed under the MIT license (`LICENSE-qutebits.mit` `LICENSE-emichael.mit` and `LICENSE-bamos.mit`) and include a re-write of `generate.py` and template restructuring.

