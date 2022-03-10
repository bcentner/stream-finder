export default {
  data: () => ({
    inputSearch: "",
    userSearched: false,
    resultArray: [
      {"title":"Inception", "director":"Christopher Nolan", "releaseDate": "2011", "posterPath": "insertURL1", "streamingProviders": ["Hulu", "Netflix"]}, 
      {"title":"Interstellar", "director":"Christopher Nolan", "releaseDate": "2017", "posterPath": "insertURL2", "streamingProviders": ["Showtime", "Netflix"]},
      {"title":"Imitation Game", "director":"Morten Tyldum", "releaseDate": "2014", "posterPath": "insertURL3", "streamingProviders": ["HBO Max", "Netflix"]}
    ],
  }),
  methods: {
    search() {
        console.log("inside search func with input: " + inputSearch);
        userSearched = true;
        // request based on inputSearch and populate jsonRaw

        // put actual results we want to display into resultArray

    }
  },
}