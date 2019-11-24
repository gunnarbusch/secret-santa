# Secret Santa
Small python script to perform a secret santa drawing

## Configuration
The following configurations can be applied in the `config.py`

|      Name      |                                    Description                                    |
|---------------:|:----------------------------------------------------------------------------------|
|  output_folder |                            Folder to write output files                           |
|  participants  |                            Participants of the drawing                            |
|  not_together  |                     Partners that should not be drawn together                    |
| output_message | The message that is outputed in the files (Available placeholders: `name`, `partner`) |

## RUN
To run secret santa script : `python secretSanta.py`

## TESTING
To run tests: `python -m unittest discover -p "*_test.py"`