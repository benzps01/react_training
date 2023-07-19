import axios from "axios";

const searchImages = async ({ searchterm }) => {
  const response = await axios.get("https://api.unsplash.com/search/photos", {
    headers: {
      Authorization: "Client-ID hdsLFoKBSs2cMjlbo1lV3BGC6sGLnOEnomZgtvwA5mA",
    },
    params: {
      query: searchterm,
    },
  });

  return response.data.results;
};

export default searchImages;
