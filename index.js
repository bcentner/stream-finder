import { createApp } from 'vue';

const app = createApp({
  data: () => ({
    inputSearch: "",
    userSearched: false,
    jsonRaw: null,
    resultArray: [],
  }),
  methods: {
    search:function() {
        console.log("inside search func with input: " + inputSearch);
        userSearched = false;
        // request based on inputSearch and populate jsonRaw

        // put actual results we want to display into resultArray

    }
  },
})

app.mount('#app');