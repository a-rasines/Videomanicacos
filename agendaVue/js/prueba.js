new Vue({
    el: '#vue_controller',
    data: {
      newContacto: {nombre: '', email: '', telefono: '' },
      agenda: [],
      no_contactos: ''
    },
    mounted: function() {
      this.cargarAgenda();
    },
  
    methods: {
      cargarAgenda: function() {
        var initAgenda = [
            {nombre: 'Juan Alvarez', email: 'juan.alvarez@gmail.com', telefono: '660 111 111' },
            {nombre: 'Pepe Lotas', email: 'pepelotas5@gmail.es', telefono: '660 222 222' },
            {nombre: 'Lorenzo Díaz', email: 'diazzlorenzo.24@gmail.com', telefono: '660 333 333' }
     
        ];
        this.agenda = initAgenda;
        if(this.agenda[0] == null){
            this.no_contactos = 'No se ha encontrado ningun contacto';
        }else{
            this.no_contactos = '';
        }
        
      },

      addContacto: function(event) {
        if(this.newContacto.nombre && this.newContacto.email && this.newContacto.telefono) {
          event.preventDefault();
          this.agenda.push(this.newContacto);
          this.newContacto = { nombre: '', email: '', telefono: '' };
          this.no_contactos = '';
        }else{
            fallo="";
            if(!this.newContacto.nombre){
                fallo += " campo:NOMBRE ";
            }
            if(!this.newContacto.email){
                fallo += " campo:EMAIL ";
            }
            if(!this.newContacto.telefono){
                fallo += " campo:TELEFONO ";
            }
            alert("**HAY CAMPOS SON RELLENAR** -->"+fallo);
        }
      },
  
      borrarContacto: function(index) {
        if(confirm("¿Seguro que quieres eliminar este contacto? Ten en cuenta que una vez hecho, no hay vuelta atras")) {
          this.agenda.splice(index, 1);        
        }
        if(this.agenda[0] == null){
            this.no_contactos = 'No se ha encontrado ningun contacto';
        }
      }
    }
  });
