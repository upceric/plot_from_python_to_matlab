marker=['+','o','*','x','s','d','^','v','>','<','p','h']
color_m=['y','m','c','r','g','b','k']
len_m=len(marker)
len_c=len(color_m)
digit=3
def plot_a_part(t='ott',kk=range(1,5),left=2,right=1014,mpv=11,title='ott'):
   #ottawa-piranha
   #kk=[2,4,6]
   #left,right=2,1014
   #AK-100
   #kk=range(1,10)
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
      #f.write('semilogy(s_'+t+'_'+str(i)+'(1:end-m).*mpv,a_'+t+'_'+str(i)+'(1:end-m).*mpv.*mpv,\''+color_m[i%len_c]+marker[i%len_m]+'-\',\'DisplayName\',[\''+str(i)+'-S=\' '+'num2str(floor(sum(sum(i_'+t+'_'+str(i)+'))/(sum(sum(d_'+t+'_'+str(i)+'))+sum(sum(i_'+t+'_'+str(i)+')))*10^'+str(digit)+')/10^'+str(digit)+')]'+',\'LineWidth\',2'+');\n')
      #f.write('plot(s_m_'+str(i)+'(1:end-m),a_m_'+str(i)+'(1:end-m),\'c'+marker[i%len_m]+'-\',\'DisplayName\',[\'m-'+str(i)+'-\' '+'num2str(sum(sum(i_m_'+str(i)+'))/(sum(sum(d_m_'+str(i)+'))+sum(sum(i_m_'+str(i)+'))))]);\n')
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
   f.write('width=1050;'+'\n')
   f.write('height=850;'+'\n')
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
   '''
   #AK-10
   kk=range(1,24)
   #kk=[2,4,9]
   f.write('mean_ak10=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_ak10_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load ak10_'+str(i)+'\n')
      f.write('mean_ak10(counter)=mean(a_ak10_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_ak10_sat(counter)=sum(i_ak10_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_ak10_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_ak10_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_ak10_'+str(i)+'(1:end-m),a_ak10_'+str(i)+'(1:end-m),\'c'+marker[i%len_m]+'-\',\'DisplayName\',[\'ak10-'+str(i)+'-\' '+'num2str(sum(sum(i_ak10_'+str(i)+'))/(sum(sum(d_ak10_'+str(i)+'))+sum(sum(i_ak10_'+str(i)+'))))]);\n')
      #f.write('plot(s_o_'+str(i)+'(1:end-m),a_o_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'o-'+str(i)+'-\' '+'num2str(sum(sum(i_o_'+str(i)+'))/(sum(sum(d_o_'+str(i)+'))+sum(sum(i_o_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   #f.write('semilogy(s_o_'+str(kk[0])+'(1:end-m),i_o_'+str(kk[0])+'(1:end-m)+d_o_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'o-void-phase\');\n')
   f.write('plot(s_ak10_'+str(kk[0])+'(1:end-m),i_ak10_'+str(kk[0])+'(1:end-m)+d_ak10_'+str(kk[0])+'(1:end-m)'+',\'c-\',\'DisplayName\',\'ak1000-void-phase\');\n')
   f.write('hold on\n')
   #AK-1000
   kk=range(1,12)
   #kk=[2,4,9]
   f.write('mean_ak1000=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_ak1000_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load ak1000_'+str(i)+'\n')
      f.write('mean_ak1000(counter)=mean(a_ak1000_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_ak1000_sat(counter)=sum(i_ak1000_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_ak1000_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_ak1000_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_ak1000_'+str(i)+'(1:end-m),a_ak1000_'+str(i)+'(1:end-m),\'y'+marker[i%len_m]+'-\',\'DisplayName\',[\'ak1000-'+str(i)+'-\' '+'num2str(sum(sum(i_ak1000_'+str(i)+'))/(sum(sum(d_ak1000_'+str(i)+'))+sum(sum(i_ak1000_'+str(i)+'))))]);\n')
      #f.write('plot(s_o_'+str(i)+'(1:end-m),a_o_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'o-'+str(i)+'-\' '+'num2str(sum(sum(i_o_'+str(i)+'))/(sum(sum(d_o_'+str(i)+'))+sum(sum(i_o_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   #f.write('semilogy(s_o_'+str(kk[0])+'(1:end-m),i_o_'+str(kk[0])+'(1:end-m)+d_o_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'o-void-phase\');\n')
   #f.write('plot(s_ak1000_'+str(kk[0])+'(1:end-m),i_ak1000_'+str(kk[0])+'(1:end-m)+d_ak1000_'+str(kk[0])+'(1:end-m)'+',\'g-\',\'DisplayName\',\'ak1000-void-phase\');\n')
   f.write('hold on\n')

   #AK-100
   kk=range(1,10)
   #kk=[2,4,9]
   f.write('mean_ak100=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_ak100_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load ak100_'+str(i)+'\n')
      f.write('mean_ak100(counter)=mean(a_ak100_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_ak100_sat(counter)=sum(i_ak100_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_ak100_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_ak100_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_ak100_'+str(i)+'(1:end-m),a_ak100_'+str(i)+'(1:end-m),\'g'+marker[i%len_m]+'-\',\'DisplayName\',[\'ak100-'+str(i)+'-\' '+'num2str(sum(sum(i_ak100_'+str(i)+'))/(sum(sum(d_ak100_'+str(i)+'))+sum(sum(i_ak100_'+str(i)+'))))]);\n')
      #f.write('plot(s_o_'+str(i)+'(1:end-m),a_o_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'o-'+str(i)+'-\' '+'num2str(sum(sum(i_o_'+str(i)+'))/(sum(sum(d_o_'+str(i)+'))+sum(sum(i_o_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   #f.write('semilogy(s_o_'+str(kk[0])+'(1:end-m),i_o_'+str(kk[0])+'(1:end-m)+d_o_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'o-void-phase\');\n')
   #f.write('plot(s_ak100_'+str(kk[0])+'(1:end-m),i_ak100_'+str(kk[0])+'(1:end-m)+d_ak100_'+str(kk[0])+'(1:end-m)'+',\'g-\',\'DisplayName\',\'ak100-void-phase\');\n')
   f.write('hold on\n')

   left,right=1,350
   #OTS beads
   kk=range(1,10)
   #kk=[2,4,9]
   f.write('mean_OTS=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_OTS_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load o_'+str(i)+'\n')
      f.write('mean_OTS(counter)=mean(a_o_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_OTS_sat(counter)=sum(i_o_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_o_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_o_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_o_'+str(i)+'(1:end-m),a_o_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'o-'+str(i)+'-\' '+'num2str(sum(sum(i_o_'+str(i)+'))/(sum(sum(d_o_'+str(i)+'))+sum(sum(i_o_'+str(i)+'))))]);\n')
      #f.write('plot(s_o_'+str(i)+'(1:end-m),a_o_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'o-'+str(i)+'-\' '+'num2str(sum(sum(i_o_'+str(i)+'))/(sum(sum(d_o_'+str(i)+'))+sum(sum(i_o_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   f.write('semilogy(s_o_'+str(kk[0])+'(1:end-m),i_o_'+str(kk[0])+'(1:end-m)+d_o_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'o-void-phase\');\n')
   #f.write('plot(s_o_'+str(kk[0])+'(1:end-m),i_o_'+str(kk[0])+'(1:end-m)+d_o_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'o-void-phase\');\n')
   f.write('hold on\n')
   '''

   '''
   left,right=1,420
   #glass beads
   kk=range(1,20,3)+range(25,33,3)
   #kk=[2,10,20]
   f.write('mean_glass=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_glass_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load g_'+str(i)+'\n')
      f.write('mean_glass(counter)=mean(a_g_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_glass_sat(counter)=sum(i_g_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_g_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_g_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_g_'+str(i)+'(1:end-m),a_g_'+str(i)+'(1:end-m),\'b'+marker[i%len_m]+'-\',\'DisplayName\',[\'g-'+str(i)+'-\' '+'num2str(sum(sum(i_g_'+str(i)+'))/(sum(sum(d_g_'+str(i)+'))+sum(sum(i_g_'+str(i)+'))))]);\n')
      #f.write('plot(s_g_'+str(i)+'(1:end-m),a_g_'+str(i)+'(1:end-m),\'r'+marker[i%len_m]+'-\',\'DisplayName\',[\'g-'+str(i)+'-\' '+'num2str(sum(sum(i_g_'+str(i)+'))/(sum(sum(d_g_'+str(i)+'))+sum(sum(i_g_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   f.write('semilogy(s_g_'+str(kk[0])+'(1:end-m),i_g_'+str(kk[0])+'(1:end-m)+d_g_'+str(kk[0])+'(1:end-m)'+',\'b-\',\'DisplayName\',\'g-void-phase\');\n')
   #f.write('plot(s_g_'+str(kk[0])+'(1:end-m),i_g_'+str(kk[0])+'(1:end-m)+d_g_'+str(kk[0])+'(1:end-m)'+',\'r-\',\'DisplayName\',\'g-void-phase\');\n')
   f.write('hold on\n')

   '''
   '''
   #phirahnia
   kk=range(2,9)
   #kk=[2,4,6]
   f.write('mean_phi=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_phi_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load p_'+str(i)+'\n')
      f.write('mean_phi(counter)=mean(a_p_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_phi_sat(counter)=sum(i_p_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_p_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_p_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_p_'+str(i)+'(1:end-m),a_p_'+str(i)+'(1:end-m),\'k'+marker[i%len_m]+'-\',\'DisplayName\',[\'p-'+str(i)+'-S_i=\' '+'num2str(sum(sum(i_p_'+str(i)+'))/(sum(sum(d_p_'+str(i)+'))+sum(sum(i_p_'+str(i)+'))))]);\n')
      #f.write('plot(s_p_'+str(i)+'(1:end-m),a_p_'+str(i)+'(1:end-m),\'k'+marker[i%len_m]+'-\',\'DisplayName\',[\'p-'+str(i)+'-\' '+'num2str(sum(sum(i_p_'+str(i)+'))/(sum(sum(d_p_'+str(i)+'))+sum(sum(i_p_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   f.write('semilogy(s_p_'+str(kk[0])+'(1:end-m),i_p_'+str(kk[0])+'(1:end-m)+d_p_'+str(kk[0])+'(1:end-m)'+',\'k-\',\'DisplayName\',\'p-void-phase\');\n')
   #f.write('plot(s_p_'+str(kk[0])+'(1:end-m),i_p_'+str(kk[0])+'(1:end-m)+d_p_'+str(kk[0])+'(1:end-m)'+',\'k-\',\'DisplayName\',\'p-void-phase\');\n')
   f.write('hold on\n')
   '''
   '''
   #basalt beads
   kk=range(1,20,3)+[25]+range(30,44,3)
   #kk=[4,10,25]
   f.write('mean_basalt=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_basalt_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load b_'+str(i)+'\n')
      f.write('mean_basalt(counter)=mean(a_b_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_basalt_sat(counter)=sum(i_b_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_b_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_b_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_b_'+str(i)+'(1:end-m),a_b_'+str(i)+'(1:end-m),\'m'+marker[i%len_m]+'-\',\'DisplayName\',[\'b-'+str(i)+'-\' '+'num2str(sum(sum(i_b_'+str(i)+'))/(sum(sum(d_b_'+str(i)+'))+sum(sum(i_b_'+str(i)+'))))]);\n')
      #f.write('plot(s_b_'+str(i)+'(1:end-m),a_b_'+str(i)+'(1:end-m),\'m'+marker[i%len_m]+'-\',\'DisplayName\',[\'b-'+str(i)+'-\' '+'num2str(sum(sum(i_b_'+str(i)+'))/(sum(sum(d_b_'+str(i)+'))+sum(sum(i_b_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   f.write('semilogy(s_b_'+str(kk[0])+'(1:end-m),i_b_'+str(kk[0])+'(1:end-m)+d_b_'+str(kk[0])+'(1:end-m)'+',\'m-\',\'DisplayName\',\'b-void-phase\');\n')
   f.write('hold on\n')
   '''
   '''
   #mix
   kk=range(1,11)
   #kk=[2,4,6]
   f.write('mean_m=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_m_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load m_'+str(i)+'\n')
      f.write('mean_m(counter)=mean(a_m_'+str(i)+'('+str(left)+':'+str(right)+'))'+';\n')
      f.write('mean_m_sat(counter)=sum(i_m_'+str(i)+'('+str(left)+':'+str(right)+'))/(sum(d_m_'+str(i)+'('+str(left)+':'+str(right)+'))+sum(i_m_'+str(i)+'('+str(left)+':'+str(right)+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('semilogy(s_m_'+str(i)+'(1:end-m),a_m_'+str(i)+'(1:end-m),\'c'+marker[i%len_m]+'-\',\'DisplayName\',[\'m-'+str(i)+'-\' '+'num2str(sum(sum(i_m_'+str(i)+'))/(sum(sum(d_m_'+str(i)+'))+sum(sum(i_m_'+str(i)+'))))]);\n')
      #f.write('plot(s_m_'+str(i)+'(1:end-m),a_m_'+str(i)+'(1:end-m),\'c'+marker[i%len_m]+'-\',\'DisplayName\',[\'m-'+str(i)+'-\' '+'num2str(sum(sum(i_m_'+str(i)+'))/(sum(sum(d_m_'+str(i)+'))+sum(sum(i_m_'+str(i)+'))))]);\n')
      f.write('hold on\n')
   f.write('semilogy(s_m_'+str(kk[0])+'(1:end-m),i_m_'+str(kk[0])+'(1:end-m)+d_m_'+str(kk[0])+'(1:end-m)'+',\'c-\',\'DisplayName\',\'m-void-phase\');\n')
   #f.write('plot(s_m_'+str(kk[0])+'(1:end-m),i_m_'+str(kk[0])+'(1:end-m)+d_m_'+str(kk[0])+'(1:end-m)'+',\'k-\',\'DisplayName\',\'m-void-phase\');\n')
   f.write('hold on\n')
   f.write('ylim([70 250000]);\n')
   f.write('ylabel(\'Mean finger area\');\n')
   f.write('xlabel(\'z-slice\');\n')
   f.write('legend(\'show\');\n')
   '''
   '''
   #ottawa-piranha
   kk=range(1,5)
   #kk=[2,4,6]
   left,right=2,1014
   f.write('mean_ott=zeros('+str(len(kk))+',1);'+'\n')
   f.write('mean_ott_sat=zeros('+str(len(kk))+',1);'+'\n')
   f.write('counter=1;'+'\n')
   for i in kk:
      f.write('load ott_'+str(i)+'\n')
      f.write('right=length(a_ott_'+str(i)+');'+'\n')
      f.write('mean_ott(counter)=mean(a_ott_'+str(i)+'('+str(left)+':right))'+';\n')
      f.write('mean_ott_sat(counter)=sum(i_ott_'+str(i)+'('+str(left)+':right'+'))/(sum(d_ott_'+str(i)+'('+str(left)+':right'+'))+sum(i_ott_'+str(i)+'('+str(left)+':right'+')))'+';\n')
      f.write('counter=counter+1;'+'\n')
      f.write('if '+str(i)+'=='+str(kk[0])+'\n')
      f.write('semilogy(s_ott_'+str(kk[0])+'(1:end-m).*mpv,i_ott_'+str(kk[0])+'(1:end-m).*mpv.*mpv+d_ott_'+str(kk[0])+'(1:end-m).*mpv.*mpv'+',\'r-\',\'LineWidth\',4,\'DisplayName\',\'pore-area\');\n')
      f.write('end'+'\n')
      f.write('hold on\n')
      #seclect a range for analysis
      f.write('a_ott_'+str(i)+'=ave_o_N(a_ott_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('i_ott_'+str(i)+'=ave_o_N(i_ott_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('d_ott_'+str(i)+'=ave_o_N(d_ott_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('s_ott_'+str(i)+'=ave_o_N(s_ott_'+str(i)+'('+str(left)+':'+str(right)+'),N)'+';\n')
      f.write('semilogy(s_ott_'+str(i)+'(1:end-m).*mpv,a_ott_'+str(i)+'(1:end-m).*mpv.*mpv,\''+color_m[i%len_c]+marker[i%len_m]+'-\',\'DisplayName\',[\''+str(i)+'-S=\' '+'num2str(floor(sum(sum(i_ott_'+str(i)+'))/(sum(sum(d_ott_'+str(i)+'))+sum(sum(i_ott_'+str(i)+')))*10^'+str(digit)+')/10^'+str(digit)+')]'+',\'LineWidth\',2'+');\n')
      #f.write('plot(s_m_'+str(i)+'(1:end-m),a_m_'+str(i)+'(1:end-m),\'c'+marker[i%len_m]+'-\',\'DisplayName\',[\'m-'+str(i)+'-\' '+'num2str(sum(sum(i_m_'+str(i)+'))/(sum(sum(d_m_'+str(i)+'))+sum(sum(i_m_'+str(i)+'))))]);\n')
      f.write('hold on\n')
      f.write('legend(\'show\');\n')
      f.write('ylim([10^4 2*10^7]);\n')
      f.write('xlabel(\'Length in vertical direction(\mum)\',\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('ylabel(\'Mean finger area(\mum^2)\',\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('set(gca,\'Fontsize\',18,\'FontWeight\',\'bold\');\n')
      f.write('legend(\'Location\',\'northeastoutside\');\n')
      f.write('\n\n\n')
      import os
      path=os.getcwd()+'/ott_pir'
      if not os.path.exists(path):
         os.makedirs(path)
      f.write('pause'+'\n')
      #f.write('saveas(gcf,\''+path+'/ott_pir_'+str(i)+'.eps\')'+'\n')
      f.write('hgexport(gcf,\''+path+'/ott_pir_'+str(i)+'.jpg\',hgexport(\'factorystyle\'),\'Format\',\'jpeg\')'+'\n')
   '''
   '''
   f.write('figure;\n')
   #f.write('plot(mean_ak10_sat,mean_ak10,\'c-o\',\'DisplayName\',\'AK1000\');\n')
   f.write('loglog(mean_ak10_sat,mean_ak10,\'c-o\',\'DisplayName\',\'AK10\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_ak100_sat,mean_ak100,\'m-o\',\'DisplayName\',\'AK100\');\n')
   f.write('loglog(mean_ak100_sat,mean_ak100,\'g-o\',\'DisplayName\',\'AK100\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_ak1000_sat,mean_ak1000,\'g-o\',\'DisplayName\',\'AK1000\');\n')
   f.write('loglog(mean_ak1000_sat,mean_ak1000,\'y-o\',\'DisplayName\',\'AK1000\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_basalt_sat,mean_basalt,\'m-o\',\'DisplayName\',\'Basalt\');\n')
   f.write('loglog(mean_basalt_sat,mean_basalt,\'m-o\',\'DisplayName\',\'Basalt\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_glass_sat,mean_glass,\'r-x\',\'DisplayName\',\'Glass\');\n')
   f.write('loglog(mean_glass_sat,mean_glass,\'r-x\',\'DisplayName\',\'Glass\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_phi_sat,mean_phi,\'k-*\',\'DisplayName\',\'Pi\');\n')
   f.write('loglog(mean_phi_sat,mean_phi,\'k-*\',\'DisplayName\',\'Piranha\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_OTS_sat,mean_OTS,\'b-+\',\'DisplayName\',\'OTS\');\n')
   f.write('loglog(mean_OTS_sat,mean_OTS,\'b-+\',\'DisplayName\',\'OTS\');\n')
   f.write('hold on\n')
   #f.write('plot(mean_OTS_sat,mean_OTS,\'b-+\',\'DisplayName\',\'OTS\');\n')
   f.write('loglog(mean_m_sat,mean_m,\'c-d\',\'DisplayName\',\'mixed\');\n')
   f.write('hold on\n')
   #f.write('ylim([70 150000]);\n')
   f.write('ylabel(\'Mean of mean finger area\');\n')
   f.write('xlabel(\'Saturation\');\n')
   f.write('legend(\'show\');\n')
   '''
   
