function [result]=ave_o_N(arr,N)
%m file for rolling average of the dataset arr,
%N is the number of data that you would like to have a mean
L=length(arr);
result=zeros(length(arr),1);
for i=1:L
result(i)=mean(arr(max(i-ceil(N/2),1):min(i+ceil(N/2),L)));
end
