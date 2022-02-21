var resultView = new Vue({
  el:'#app',
  data() {
    return {
      inputSearch: "",
      userSearched: false,
      jsonRaw: null,
      resultArray: [],
    }
  },
  methods: {
    search:function() {
        userSearched = true;
        // request based on inputSearch and populate jsonRaw

        // put actual results we want to display into resultArray

    }
  },
})