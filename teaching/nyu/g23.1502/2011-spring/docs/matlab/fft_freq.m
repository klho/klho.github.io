%FFT_FREQ  Compute a FFT restricted to non-negative frequencies and return
%          the frequencies associated with each Fourier component.
%
%   X = FFT_FREQ(X,T,DT) returns the discrete Fourier transform of X
%   sampled over the time interval T in time increments of DT, restricted
%   to non-negative frequencies only. The time interval T must have the
%   form [TMIN, ..., TMAX]; only the first and last elements are used.
%
%   [X,W] = FFT_FREQ(X,T,DT) also returns the frequencies W associated with
%   each component of X.
%
%   See also FFT.
function [X, w] = fft_freq(x, t, dt)
    n = ceil((t(end) - t(1)) / dt);
    nfft = 2^nextpow2(n);
    X = fft(x,nfft) / n;
    X = X(1:ceil(nfft/2));
    w = 1/(2*dt) * linspace(0, 1, ceil(nfft/2));
end