const states = {
  on: {
    text: "ON",
    color:"green"
  },
  off: {
    text: "OFF",
    color: "red"
  },
  unkn: {
    text: "UNKN",
    color: "grey"
  }
}

function execute(action) {
  return $.get(`/action/${ action.module }/${ action.action }/`);
}

Vue.component("light-switch", {
  props: ["light"],

  data: function () {
    return {
      id: this.light.id,
      state: states.unkn,
    }
  },

  template: `
    <div class="switch" 
      :style="{ backgroundColor: this.state.color }"
      v-on:click="toggle()"
    >
      <h3 class="switch-title">{{ light.name }}</h3>
      <h1 class="switch-status">{{ this.state.text }}</h1>
    </div>`,

  methods: {
    toggle: function() { 
      // Toggle switch status
      if (this.state === states.on) {
        execute({ module: this.id, action: "off"});
        this.state = states.off;
      } else if (this.state === states.off) {
        execute({ module: this.id, action: "on"});
        this.state = states.on;
      }
    }
  },
  
  mounted: function() {
    // Get switch status
    var request = { module: this.id, action: "status"}
    execute(request).done((data) => {
      if (data.indexOf("on") > -1) {
        this.state = states.on;
      } else if (data.indexOf("off") > -1) {
        this.state = states.off;
      }
    });
  }
  
});


var app = new Vue({
  el: "#app",
  data: {
    switches: [
      {id: "bedlight", name: "Bed Light"},
      {id: "livingroom", name: "Living Room"},
      {id: "catlight", name: "Cat Light"}
    ],
    
    buttons: [
      {id: "vmpower", text:"Power VM 150", action:"vm/power150"},
      {id: "wake", text:"Wake Server", action:"desktop/wake"},
      {id: "shutdown", text: "Power off Controller", action:""}
    ],

  },

  methods: {
    onSwitched: function(id) {
      console.log("light function called");
      console.log(id);
      execute("hello there");
    },

    goToList: function() {
      window.location.href = "/list.html"
    }
  }
});

