import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api"

export default class CafeApi {
    static async fetchCafes() {
        const response = await axios.get(`${API_BASE_URL}/cafes/`)
        return response.data
        }
    }