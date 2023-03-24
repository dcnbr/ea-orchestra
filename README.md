# Installation

## Dependencies
- Python 3
- Numpy
- Scipy
- [librosa](https://librosa.org/doc/latest/index.html)

Ideally, just do:
```
~$ pip install numpy scipy librosa
```

# Running
```
~$ python3 main.py <config.ini>
```

# Configuration file

Structure is:

```ini
[general]
input_audio = <path/to/input/audio.wav>
output_audio = <path/to/output/audio.wav>
...

[fitness]
strategy_name = <name of python function in fitness.py to use>
parameter_1 = <first hyperparameter needed by funtion>
parameter_2 = <second hyperparameter>
...
parameter_n = <last hyperparameter>

[mutation]
strategy_name = <name of python function in mutation.py to use>
parameter_1 = <>
...

[crossover]
strategy_name = <name of python function in crossover.py to use>
parameter_1 = <>
...

[parents]
strategy_name = <name of python function in parents.py to use>
parameter_1 = <>
...

[survivors]
strategy_name = <name of python function in survivors.py to use>
parameter_1 = <>
...

```

# Implementing New Strategies

In theory, this will be very similar to how it worked in the class assignment.
The only difference should be how the hyperparameters are passed to the
functions. Rather than being passed as multiple input parameters, they will now
be passed as a python dictionany of key:value pairs.

For example, consider implementing tournament-based parent selection.
Tournament selection requires two hyper-parameters, `mating_pool_size` and
`tournament_size`, as well as the population's `fitness`.\_

In the `configuration.ini` file:
```ini
[general]
...

[parents]
strategy_name = tournament
mating_pool_size = 100
tournament_size = 10

...
```

In `parents.py`:
```python
def tournament(fitness, hyperparams)
	mating_pool_size = int(hyperparams['mating_pool_size'])
	tournament_size = int(hyperparams['tournament_size'])

	...
	# algorithm for tournament selection
	...

	# return list of indexes that correspond to those chosen to mate
	return selected_to_mate

```

## Note on genotypes/representation

An individual is a 3-tuple:
```python
(frequency, amplitude, phase)
```
Where
1. `frequency` is a number between [0 .. 11025]
2. `amplitude` is a number between [0 .. Infinity]
3. `phase` is a number between [0 .. 2pi]

These are the ranges of the input signal, and must be the range of the
output signal. Its okay if individuals in the population of the ea go outside
these ranges, but (a) they will be rounded up/down to fit when turned back into
audio, and (b) going outside will probably be a low fitness thing to do anyways.


