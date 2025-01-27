program volumen;
uses crt;
const
pi=3.1416;
a=1.33;
r=3;
var
v: double;
begin
    write ('obten el voluemn de una esfera de 3cm');
    read;
    v:=a*pi*(r*r*r);
    write ('El volumen es:', v:1:2 ,'cm');
    readkey;
End.
