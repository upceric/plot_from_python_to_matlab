marker=['+','o','*','x','s','d','^','v','>','<','p','h']
color_m=['y','m','c','r','g','b','k']
len_m=len(marker)
len_c=len(color_m)
digit=3 #keep three digits
def plot_a_part(t='ott',kk=range(1,5),left=2,right=1014,mpv=11,title='ott'):
   '''
   sub function to generate matlab file for plot
   '''
   #kk=[2,4,6]
   #left,right=2,1014
   #AK-100 #kk=range(1,10)
   #kk=[2,4,9]
   #f.write('C=linspecer('+str(len(kk)+1)+',\'sequential\');'+'\n')
   f.write('C=distinguishable_colors('+str(len(kk)+1)+');'+'\n')
   f.write('mean_'+t+'=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_'+t+'_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load '+t+'_'+str(i)+'\n')
      f.write('right=length(a_'+t+'_'+str(i)+');'+'\n')
      f.write('mean_'+t+'(counter)=mean(a_'+t+'_'+str(i)+'('+str(left)+':right))'+';\n')
      f.write('mean_'+t+'_sat(counter)=sum(i_'+t+'_'+str(i)+'('+str(left)+':right'+'))/(sum(d_'+t+'_'+str(i)+'('+str(left)+':right'+'))+sum(i_'+t+'_'+str(i)+'('+str(left)+':right'+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('if '+str(i)+'=='+str(kk[0])+'\n')
      f.write('semilogy(s_'+t+'_'+str(kk[0])+'(1:end-m).*mpv,i_'+t+'_'+str(kk[0])+'(1:end-m).*mpv.*mpv+d_'+t+'_'+str(kk[0])+'(1:end-m).*mpv.*mpv'+',\'r\',\'LineWidth\',4,\'DisplayName\',\'pore-area\');\n')
      f.write('end'+'\n')
      f.write('hold on\n')
      #seclect a range for analysis
      f.write('a_'+t+'_'+str(i)+'=ave_o_N(a_'+t+'_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('i_'+t+'_'+str(i)+'=ave_o_N(i_'+t+'_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('d_'+t+'_'+str(i)+'=ave_o_N(d_'+t+'_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('s_'+t+'_'+str(i)+'=ave_o_N(s_'+t+'_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('semilogy(s_'+t+'_'+str(i)+'(1:end-m).*mpv,a_'+t+'_'+str(i)+'(1:end-m).*mpv.*mpv,'+'\'color\',C(counter-1,:)'+',\'DisplayName\',[num2str(counter-1) \'-S=\' '+'num2str(floor(sum(sum(i_'+t+'_'+str(i)+'))/(sum(sum(d_'+t+'_'+str(i)+'))+sum(sum(i_'+t+'_'+str(i)+')))*10^'+str(digit)+')/10^'+str(digit)+')]'+',\'LineWidth\',4'+');\n')
      f.write('hold on\n')
      f.write('set(gca,\'linewidth\',4,\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('title(\''+title+'\',\'interpreter\',\'latex\');\n')
      f.write('right_b=max(i_'+t+'_'+str(kk[0])+'(1:end-m).*mpv.*mpv+d_'+t+'_'+str(kk[0])+'(1:end-m).*mpv.*mpv);'+'\n')
      f.write('ylim([10^4 right_b*2]);\n')
      f.write('xlabel(\'Length in vertical direction(\mum)\',\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('ylabel(\'Mean finger area(\mum^2)\',\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('legend(\'Location\',\'northeastoutside\');\n')
      f.write('h1=legend(\'show\');\n')
      f.write('set(h1,\'Fontsize\',12);\n')
      f.write('\n\n\n')
      import os
      path=os.getcwd()+'/'+t+'_pir'
      if not os.path.exists(path):
         os.makedirs(path)
      #f.write('pause'+'\n')
      #f.write('saveas(gcf,\''+path+'/ott_pir_'+str(i)+'.eps\')'+'\n')
      f.write('hgexport(gcf,\''+path+'/'+t+'_pir_'+str(i)+'.eps\',hgexport(\'factorystyle\'),\'Format\',\'eps\')'+'\n')
      f.write('hgexport(gcf,\''+path+'/'+t+'_pir_'+str(i)+'.jpg\',hgexport(\'factorystyle\'),\'Format\',\'jpeg\')'+'\n')
 
with open('plot_batch_all.m','w') as f:
   f.write('m=0;'+'\n')
   f.write('h=figure'+'\n')
   f.write('mpv=11;'+'\n')
   left,right=1,420
   f.write('x0=10;'+'\n')
   f.write('y0=10;'+'\n')
   f.write('width=1050;'+'\n')#set the picture x range
   f.write('height=850;'+'\n')#set the picture y range
   f.write('N=7;'+'\n')
   f.write('set(gcf,\'units\',\'points\',\'position\',[x0,y0,width,height]);'+'\n')
   #AK-100
   kk=range(1,10)
   #kk=[2,4,9]
   left,right=1,540
   #plot_a_part('ak100',kk=kk,left=left,right=right,mpv=11,title='AK100-water-glass-$$135^\circ(\pm 15^\circ)$$')

   #AK-1000
   kk=range(2,12)
   #kk=[2,4,9]
   left,right=1,540
   #plot_a_part('ak1000',kk=kk,left=left,right=right,mpv=11,title='AK1000-water-glass-$$140^\circ(\pm 15^\circ)$$')

   #ottawa-piranha
   kk=range(1,5)
   #kk=[2,4,6]
   left,right=2,1014
   #plot_a_part('ott',kk=kk,left=left,right=right,mpv=11,title='Dodecane-water-Ott_sand-$$165^\circ(\pm 15^\circ)$$')

   #mix
   kk=range(1,11)
   #kk=[2,4,6]
   left,right=1,540
   #plot_a_part('m',kk=kk,left=left,right=right,mpv=11,title='AK0.65-water-glass-$$90^\circ(\pm 10^\circ)$$')

   #glass beads
   #kk=range(1,20,3)+range(25,33,3)
   kk=range(1,20)+range(25,33)
   left,right=1,540
   #plot_a_part('g',kk=kk,left=left,right=right,mpv=11,title='Dodecane-water-glass-$$125^\circ(\pm 15^\circ)$$')

   #phirahnia
   kk=range(2,9)
   #kk=[2,4,6]
   left,right=1,540
   #plot_a_part('p',kk=kk,left=left,right=right,mpv=11,title='Air-water-glass-$$20^\circ(\pm 10^\circ)$$')

   #OTS beads
   kk=range(1,10)
   #kk=[2,4,9]
   left,right=1,450
   #plot_a_part('o',kk=kk,left=left,right=right,mpv=11,title='Dodecane-water-glass(OTS)-$$165^\circ(\pm 15^\circ)$$')

   #basalt beads
   kk=range(1,20,2)+[25]+range(30,44,2)
   #kk=range(1,20)+[25]+range(30,44)
   #kk=[4,10,25]
   left,right=1,540
   #plot_a_part('b',kk=kk,left=left,right=right,mpv=11,title='Dodecane-Water-basalt-$$75^\circ(\pm 15^\circ)$$')
