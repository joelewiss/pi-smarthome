function execute(action) {
  return `executed action ${action}`
}

Vue.component("light-switch", {
  props: ["light"],

  data: function () {
    return { 
      on: false,
      colors: {
        on: "green",
        off: "red",
        unkn: "grey"
      },
    }
  },

  template: `
    <div class="switch" 
      :style="{ backgroundColor: colors.unkn }"
      v-on:click="$emit('switched', light.id)"
    >
      <h3 class="switch-title">{{ light.name }}</h3>
      <h1 class="switch-status">UNKN</h1>
    </div>`,

  methods: {
  },
  
  mounted: function() {
    console.log("mounted lightswitch component");
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

