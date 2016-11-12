%% initialize
f = @(t)(    sin(2*pi*10*t) + ...   % input signal
          2 *sin(2*pi*20*t) - ...
         0.7*sin(2*pi*30*t));
T = 10;                             % sampling time interval
dt = 0.01;                          % sampling time period
%% compute
n = ceil(T/dt);                     % number of sample points
t = linspace(0, T, n);              % sampling times
x = f(t) + randn(1,n);              % sampled noisy signal
[X, w] = fft_freq(x, t, dt);        % compute FFT
%% plot
figure
plot(w, abs(X))                     % frequency contributions
xlabel('Frequency (\omega) [Hz]')
ylabel('Fourier coefficient modulus (|F|)')