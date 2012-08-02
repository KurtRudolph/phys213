#include <stdio.h>
#include <math.h>

int main(){

  double  T = 235.,
          Delta_1 = .1,
          Delta_2 = .15,
          M_1 = 60000.,
          M_2 = 20000.,
          N = 900.;

//-Delta_1 + k_b * T * ln( N_1 / M_1) = -Delta_2 + k_b * T * ln( (900 - N_1) / M_2)
//N_1 + N_2 = N

//( N_1 / M_1) / ((N - N_1) / M_2) = e^((-Delta_2 + Delta_1) / (k_b * T))

double N_1 = N * M_1 * exp(