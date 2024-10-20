import { defineStore } from "pinia";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: {
      isAuthenticated: false,
      email: null as string | null,
      token: null as string | null,
    },
  }),

  actions: {
    initStore() {
      this.user.isAuthenticated = false;

      const token = this.getCookie("user.token");
      const email = this.getCookie("user.email");

      if (token) {
        this.user.token = token;
        this.user.email = email || null;
        this.user.isAuthenticated = true;

        console.log("Initalized user:", this.user);
      }
    },
    setToken(token: string, email: string) {
      console.log("setToken", token, email);

      this.user.token = token;
      this.user.email = email;
      this.user.isAuthenticated = true;

      // クッキーに保存（有効期限7日）
      this.setCookie("user.token", token, 7);
      this.setCookie("user.email", email, 7);
    },
    removeToken() {
      console.log("removeToken");

      this.user.token = null;
      this.user.email = null;
      this.user.isAuthenticated = false;

      // クッキーを削除
      this.setCookie("user.token", "", -1);
      this.setCookie("user.email", "", -1);
    },
    // クッキーを設定
    setCookie(name: string, value: string, days: number) {
      const expires = new Date();
      expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
      document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
    },
    // クッキーを取得
    getCookie(name: string): string | null {
      const nameEQ = name + "=";
      const ca = document.cookie.split(";");
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === " ") c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0)
          return c.substring(nameEQ.length, c.length);
      }
      return null;
    },
  },
});
