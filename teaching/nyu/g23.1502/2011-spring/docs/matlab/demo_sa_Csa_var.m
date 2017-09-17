%filename: demo_sa_Csa_var.m
clear all % clear all variables
clf       % and figures
global T TS TMAX QMAX;
global Rs Csa dt;
in_sa %initialization
Csa_list = Csa .* [2 1 0.5];
n = length(Csa_list);
t_plot = (1:klokmax)*dt;
QAo_plot = zeros(n,klokmax);
PSa_plot = zeros(n,klokmax);
for i = 1:n
    Csa = Csa_list(i);
    for klok=1:klokmax
        t=klok*dt;
        QAo=QAo_now(t);
        Psa=Psa_new(Psa,QAo); %new Psa overwrites old
        %Store values in arrays for future plotting:
        %t_plot(i,klok)=t;
        QAo_plot(i,klok)=QAo;
        Psa_plot(i,klok)=Psa;
    end
end
%Now plot results in one figure 
%with QAo(t) in upper frame
% and Psa(t) in lower frame
subplot(2,1,1)
plot(t_plot, QAo_plot(1,:), ...
     t_plot, QAo_plot(2,:), ...
     t_plot, QAo_plot(3,:))
legend(sprintf('C_{sa} = %f', Csa_list(1)), ...
       sprintf('C_{sa} = %f', Csa_list(2)), ...
       sprintf('C_{sa} = %f', Csa_list(3)))
subplot(2,1,2)
plot(t_plot, Psa_plot(1,:), ...
     t_plot, Psa_plot(2,:), ...
     t_plot, Psa_plot(3,:))
legend(sprintf('C_{sa} = %f', Csa_list(1)), ...
       sprintf('C_{sa} = %f', Csa_list(2)), ...
       sprintf('C_{sa} = %f', Csa_list(3)))
