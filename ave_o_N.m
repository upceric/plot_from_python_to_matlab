function [result]=ave_o_N(arr,N)
%return the average value of every N values
%L=length(arr);
%result=zeros(ceil(length(arr)/N),1);
%for i=1:ceil(length(arr)/N)
%result(i)=mean(arr(min(1+N*(i-1),L):min(N+N*(i-1),L)));
%end
L=length(arr);
result=zeros(length(arr),1);
for i=1:L
result(i)=mean(arr(max(i-ceil(N/2),1):min(i+ceil(N/2),L)));
end