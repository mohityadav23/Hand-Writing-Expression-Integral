function [out] = integral_string(str)

str = lower(str);

str = strrep(str,'sum','^');



str = strrep(str,'2x','2*x');
str = strrep(str,'2c','2*c');
str = strrep(str,'2s','2*s');
str = strrep(str,'2l','2*l');
str = strrep(str,'2e','2*e');
str = strrep(str,'2t','2*t');
str = strrep(str,'2(','2*(');

str = strrep(str,'3x','3*x');
str = strrep(str,'3c','3*c');
str = strrep(str,'3s','3*s');
str = strrep(str,'3l','3*l');
str = strrep(str,'3e','3*e');
str = strrep(str,'3t','3*t');
str = strrep(str,'3(','3*(');

str = strrep(str,'4x','4*x');
str = strrep(str,'4c','4*c');
str = strrep(str,'4s','4*s');
str = strrep(str,'4l','4*l');
str = strrep(str,'4e','4*e');
str = strrep(str,'4t','4*t');
str = strrep(str,'4(','4*(');

str = strrep(str,'5x','5*x');
str = strrep(str,'5c','5*c');
str = strrep(str,'5s','5*s');
str = strrep(str,'5l','5*l');
str = strrep(str,'5e','5*e');
str = strrep(str,'5t','5*t');
str = strrep(str,'5(','5*(');

str = strrep(str,'6x','6*x');
str = strrep(str,'6c','6*c');
str = strrep(str,'6s','6*s');
str = strrep(str,'6l','6*l');
str = strrep(str,'6e','6*e');
str = strrep(str,'6t','6*t');
str = strrep(str,'6(','6*(');

str = strrep(str,'7x','7*x');
str = strrep(str,'7c','7*c');
str = strrep(str,'7s','7*s');
str = strrep(str,'7l','7*l');
str = strrep(str,'7e','7*e');
str = strrep(str,'7t','7*t');
str = strrep(str,'7(','7*(');

str = strrep(str,'8x','8*x');
str = strrep(str,'8c','8*c');
str = strrep(str,'8s','8*s');
str = strrep(str,'8l','8*l');
str = strrep(str,'8e','8*e');
str = strrep(str,'8t','8*t');
str = strrep(str,'8(','8*(');

str = strrep(str,'9x','9*x');
str = strrep(str,'9c','9*c');
str = strrep(str,'9s','9*s');
str = strrep(str,'9l','9*l');
str = strrep(str,'9e','9*e');
str = strrep(str,'9t','9*t');
str = strrep(str,'9(','9*(');



str = strrep(str,'le','lo');
str = strrep(str,'la','lo');
str = strrep(str,'l0','lo');
str = strrep(str,'t0','to');
str = strrep(str, 'tog','log');
str = strrep(str,'1og','log');



str = strrep(str,'ce','co');
str = strrep(str,'ca','co');
str = strrep(str,'c0','co');

str = strrep(str,'to','ta');
str = strrep(str,'te','ta');
str = strrep(str,'tah','tan');


str = strrep(str,'ih','in');
str = strrep(str, '5in', 'sin');
str = strrep(str, 'gin', 'sin');
str = strrep(str,'sln','sin');


str = strrep(str,'cx','(x');


str = strrep(str,'(e)^(x)','exp(x)');
str = strrep(str,'(e)^(2*x)','exp(2*x)');
str = strrep(str,'(e)^(3*x)','exp(3*x)');
str = strrep(str,'(e)^(4*x)','exp(4*x)');
str = strrep(str,'(e)^(5*x)','exp(5*x)');
str = strrep(str,'(e)^(6*x)','exp(6*x)');
str = strrep(str,'(e)^(7*x)','exp(7*x)');
str = strrep(str,'(e)^(8*x)','exp(8*x)');
str = strrep(str,'(e)^(9*x)','exp(9*x)');
str = strrep(str,'(e)^(-x)','exp(-x)');


exp = sym(str) ; 
out = int(exp) ; 
