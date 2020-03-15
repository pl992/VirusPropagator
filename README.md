<h1> Virus Propagator </h1>
<h3> Real world interpretation </h3>

This simulator shows how the 'Herd immunity' develops and what is exactly.
At the end of the simulation there are no more infected people and the disease
disappears. 
The remaining people in the lattice never got infected and they will never do
because no more disease is present (some news are reporting this is the current technique 
the UK government wants to apply for the new spreading virus [COVID19](https://www.theguardian.com/commentisfree/2020/mar/15/epidemiologist-britain-herd-immunity-coronavirus-covid-19))

The dots deleted from the lattice can be interpreted in 3 different ways:

* They got killed by the virus

* They had been quarantined

* They healed

<h3> Just run the script </h3>

Running the script will make a simple animation (in
the running folder) called Movie.mp4. If the settings
are similar yellow dots will represent infected people and
the others healthy people. 
Play with the parameters. The information of the simulation
will be saved in the worlds directory such that analysis can be done
afterwards. 
<h3> Simulation details </h3>

2D lattice with spacexspace cells representing the space

Each cell of the grid can be contaminated or not contaminated. 
After dt iterations a cell is contaminated it comes back to be not 
contaminated

It starts from a population of npeople people with ninfected infected dots.

People are moving through random walks (dispacement defines the 
size of the square inside which the dot can move)

If an infected person passes through a not contaminated cell the 
cell becomes contaminated, if it's already contaminated the timer 
of the contamination start over

If a person not infected passes through a contaminated cell he has a 
probability of p_get_infected to get infected

After lifetime timesteps an infected person is deleted from from the grid
<h3> Main parameters </h3>

* space: number of cells the 2D lattice contains

* p_get_infected: probability that a dot passing through
an infected cell becomes infected

* lifetime: number of iterations an infected dot passes before
being removed from the lattice

* npeople: number of dots contained in the lattice

* dt: number of iterations a cell can infect the dots

* T: maximum time that will be spent

* ninfected: starting number of infected dots

* displacement: number of cells in each dimension a dot can move

