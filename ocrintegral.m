function [ P ] = ocrintegral( image )

figure;
imshow(image);

results = ocr(image);

str = results.Text;

str = lower(str);

str = strrep(str,'/\','^');

str = strrep(str,'"','^');

str = strrep(str,'e^x','exp(x)');
str = strrep(str,'e^2x','exp(2*x));

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

expression = sym(str)

P = int(expression) ;






end

