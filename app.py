from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/<chasis>', methods=['GET'])
def hello_world(chasis):
    return render_template('index.html',
                           Lblfechaemision='01/03/2023',
                           LblFechaexpiracion='01/06/2023',
                           LblNombreComprador='STARLIN MATOS MEDINA',
                           LblRnCedulaComprador='22301547836',
                           LblRnCedulaImportador='123006799',
                           LblNombreImportador='COLLADO AUTO SRL',
                           lblChasis='19XFC1F32GE041661',
                           lblYear='2016',
                           lblColor='NEGRO',
                           lblModelo='Civic',
                           lblMarca='HONDA',
                           lblTipoVehiculo='AUTOMOVIL PRIVADO',
                           lblPlaca='PP793515',
                           lblCodigo='dg9hri')

if __name__ == '__main__':
    app.run()
