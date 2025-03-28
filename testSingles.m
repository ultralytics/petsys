% Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

function [] = testSingles()
clc; close all
A=fcnloadtextfile('my_data_singles.txt');  X=A.x;
tspan=diff(minmax3(X(:,1)))/1E12;
X = calibrateEnergy(X);  na=size(X,1);

%SELECT 511keV CANDIDATES
e1=400; % (keV)
e2=600; % (keV)
i=X(:,2)>e1 & X(:,2)<e2;  X=X(i,:);  nb=sum(i);

%SET t1=0
X=sortrows(X,1);
X(:,1) = X(:,1)-X(1,1);

%FIND PAIRS
maxdt=1000; %(ps)
dt=diff(X(:,1));
a=X(2:end,3)==309;  dt(a)=-dt(a);
i=find(abs(dt)<maxdt & diff(X(:,3))~=0);  nc=numel(i);
sca; fhistogram(dt(i),50); xlabel(sprintf('dt_{%g-%g keV} (ps)',e1,e2))

fprintf('\n%g singles over %.4f seconds (%.1f Hz)\n%g energy candidate singles (%g-%g keV)\n%g dt candidate pairs (<%g ps dt)\n',na,tspan,na/tspan,nb,e1,e2,nc,maxdt);


function X = calibrateEnergy(X)
%PEAKS ARE AT: 
%511keV = 173
%1274keV = 207
%344keV = 150 (compton edge)
E=X(:,2);
px=[0 150 173 207];
py=[0 334 511 1274];
load Efits.mat

a=Exp1fit(E);  a=min(a,2000);
b=Exp2fit(E);  b=min(b,2000);
c=PCHIPfit(E); c=min(c,2000);

fig(2,3); x=linspace(0,1500,300);
sca; histogram(E,linspace(0,300,300)); xyzlabel('E (samples)')
h=sca; plot(px,py,'k.','Markersize',20,'Display','Calibration Points'); h.XLim=[0 300]; h.YLim=[0 1500];
pa=linspace(0,300,1000); plot(pa,Exp1fit(pa),'Display','Exp1 fit'); plot(pa,Exp2fit(pa),'Display','Exp2 fit'); plot(pa,PCHIPfit(pa),'Display','PCHIP fit'); 
fcnlinewidth(2); xyzlabel('E (samples)','E_{calibrated} (keV)'); legend('Location','Best')
sca; histogram(a,x);  xyzlabel('E_{Exp1 calibrated} (keV)')
sca; histogram(b,x);  xyzlabel('E_{Exp2 calibrated} (keV)')
sca; histogram(c,x);  xyzlabel('E_{PCHIP calibrated} (keV)')
X(:,2)=a;
