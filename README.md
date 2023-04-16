# yaml2latex

Generate LATEX from LATEX template and YAML specification.

An example is included in `priv/templates/cv`, that generates a CV

# Dependencies

*   Linux distro with working shell.

*   Python 3 with dependencies installed from `package.txt`.

# Usage

```
python3 src/render-tex-from-template.py \
    --latex-template priv/templates/cv-template.tex \
    --yaml priv/templates/cv.yaml > cv.tex

```

# Acknowledgements

This project is inspired by the work of [Aleksandr Mattal][mattal] and
[Brandon Amos][amos].

# License

This work is distributed under the MIT license (`LICENSE`) with
portions copyright [Aleksandr Mattal][mattal], [Brandon Amos][amos] and
[Ellis Michael][emichael] 

[mattal]: https://github.com/QuteBits/resume_42
[amos]: https://github.com/bamos/cv
[emichael]: https://github.com/emichael/resume
