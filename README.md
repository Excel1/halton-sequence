# Van der Corput Sequence Visualizer

This Python program visualizes the Van der Corput sequence, a low-discrepancy sequence used in the field of numerical
integration and for creating quasi-random point sequences. It generates 2D plots for pairs of Van der Corput sequences
with different bases and saves these plots as PNG images.

## Dependencies

- Python 3.x
- Matplotlib

Ensure that you have Python installed on your system. You can install Matplotlib using pip:

```sh
pip install matplotlib
```

## How it Works

The program defines a function `van_der_corput` that generates a Van der Corput sequence for a given number of
elements (
`n_sample`) and a base (`base`). It then iterates over a predefined list of `n` values and base pairs, generates Van der
Corput sequences for each pair of bases, and plots these sequences against each other. Each plot is saved as a PNG file
named according to the `n` value and base pair used.

## Usage

Simply run the program with Python:

```sh
python path/to/your_script/main.py
```

Make sure to adjust path/to/your_script.py to the actual path of the script on your system.

## Output

The program saves a series of PNG images in the directory where the script is run. Each image represents a plot of
points generated by two Van der Corput sequences. The file names reflect the parameters used to generate the sequences,
following the pattern `n=<n_value>b1=<base1>b2=<base2>.png`.

For example, a file named `n=7b1=3b2=5.png` corresponds to a plot generated by comparing Van der Corput sequences with
`n=7`, `base1=3`, and `base2=5`.

## Notes

- The choice of bases and `n` values in the script can significantly affect the visual outcome of the plots. Experiment with
different values to explore the behavior of Van der Corput sequences.
- The script uses the 'TkAgg' backend for Matplotlib, which is suitable for most environments. If you encounter any issues
with plotting, consider changing the Matplotlib backend as appropriate for your setup


## Sources
- https://gist.github.com/tupui/cea0a91cc127ea3890ac0f002f887bae

## License 
This project is open-source and available for personal and educational use.