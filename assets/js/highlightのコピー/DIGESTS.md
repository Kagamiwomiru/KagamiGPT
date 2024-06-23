## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
  integrity="sha384-9mu2JKpUImscOMmwjm1y6MA2YsW3amSoFNYwKeUHxaXYKQ1naywWmamEGMdviEen"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"
  integrity="sha384-WmGkHEmwSI19EhTfO1nrSk3RziUQKRWg3vO0Ur3VYZjWvJRdRnX4/scQg+S2w1fI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-TzEBCf/KQYyfWRnusn5SWj/Oc0TGXcdiZY5Jhb4eR4MYGasQ5n6SpkNDXudJ+V5R /es/languages/applescript.js
sha384-kjROxlwayCv+KEVryJVQjpjchjf7C8tyLrq7hDNnQeBXCp3+X9ZQdw9yXT8wRikI /es/languages/applescript.min.js
sha384-0OZaeLK1yb5eP3nW4y0JP1fVharSrsuv/1mkI/6/8aRFm9laYIWIMXjCOqu+vRW5 /es/languages/c.js
sha384-G7WtwjMBNGrPly3ZsbPhfnT0v88hG3Ea9fQhrSWfzj7cNAsXsU7EKMQLyLGj7vTH /es/languages/c.min.js
sha384-Wjwd1YEG/PYlkLHTWIx+RlPK6XboMN3bEpveERJ8D8Z4RaNE02Ho19ZFrSRPGi0j /es/languages/cpp.js
sha384-Q4zTNH8WsDVdSZbiZtzWS1HmAUcvMSdTmth9Uqgfjmx7Qzw6B8E3lC9ieUbE/9u4 /es/languages/cpp.min.js
sha384-DA5ii4oN8R2fsamNkHOanSjuN4v7j5RIuheQqnxMQ4cFnfekeuhwu4IdNXiCf+UU /es/languages/css.js
sha384-OBugjfIr093hFCxTRdVfKH8Oe3yiBrS58bhyYYTUQJVobk6SUEjD7pnV8BPwsr8a /es/languages/css.min.js
sha384-nJZn4t0S58K5MJ/2BOmgkTC8TtBWB76ykEKIIzb8sUxT3h7ouZH5Ucqnr9MJ6Bry /es/languages/diff.js
sha384-OIJrZgyhN1E6e29B9M3gFPtkR5JgXpls8h5D2bNzBxQ8Ncwxzfjedu3/0jZEe7S9 /es/languages/diff.min.js
sha384-/wYGIAWwdVeBvXFBq3HUPpdw6KUhW3wMMXruGXWjhlYT/IruTWojBeoPUbpGXaf5 /es/languages/dockerfile.js
sha384-DQdaFTXRCa9EQdAkBCHnMAhAomUgizSpJPmuCzoaDJMAshvgxlJF5d7J/ysvc6f/ /es/languages/dockerfile.min.js
sha384-7m427rj9OYl8KKObOk+aD0QhXmqXy6hU/sHGS6OUwW9hRiiHvr+tLTbLiSJYbIyD /es/languages/http.js
sha384-GdKwMgTrO0R3SPXhm+DuaN3Qr7WkqYmmTClINAGPuV/BUPE9WUI/WnTEntp522Sl /es/languages/http.min.js
sha384-7hMYwsnoFLW0Wnjv4vRnZxuedW1tCz7/pydl1b9w3fg7B+rldToCjqzXwCRHUE7C /es/languages/ini.js
sha384-LDu6uT3diI3jBUJtdoGFa787cYlVrR+aqFfmW+kW+TImOkpVe+P5LBdDzydIHo9Z /es/languages/ini.min.js
sha384-WCznKe2n87QvV/L1MlXN+S8R6NPUQGU34+AqogMuWGZJswSD6rt3Mgih+xuKlDgm /es/languages/javascript.js
sha384-eGsBtetyKPDKaLiTnxTzhSzTFM6A/yjHBQIj4rAMVaLPKW5tJb8U6XLr/AikCPd+ /es/languages/javascript.min.js
sha384-12GbYFzdyZCSmfBTmO2CR/qE89K5uE1PEuJ3QUwXH0Q9u+uoLNigjH9dG7LAxxiI /es/languages/json.js
sha384-+DT7AtubDhVDciRc6CgjJJRsCt0L8NC3Dh8n9Tj2tZWU8rWxDIj1ViubmUDn8OCY /es/languages/json.min.js
sha384-JZ1yKn4lHbd05rOuRoUSoCM323D+X3s7vLYhESynzVpdWAFu5JNp6chDl5N9uc1c /es/languages/latex.js
sha384-dDJ50ltJ9VlfSOzSORI0KSNPcRIpLy1J0BmtdQGXBEY+7f57DAx754HVffzmWqC2 /es/languages/latex.min.js
sha384-UgQTewauLJ4EgpADCJ99JfEtiPvw+fyaSrY1gtCVBviDNG7yCH5U7qutYptSfYk+ /es/languages/makefile.js
sha384-aUXBqKsjOzPD/W+hccF21KKWmWts/CrY/lWGJU+dAcsKtuh1/XtyDnzfLmqy/fV1 /es/languages/makefile.min.js
sha384-bWwkdmOCj83zZ8/m+oPD9goRMhrPCb25ZA6aTyg7vcsq9IpuyED38kQSw1Na4UTZ /es/languages/markdown.js
sha384-SqGSUq0DMQ0OUQnQnTuVDCJyhANd/MFNj+0PF67S+VXgHpR8A4tPsf/3GoSFRmrx /es/languages/markdown.min.js
sha384-+5oyk7Ed3OlvEWGj8xracq/6e52BScKUN4kxcreNwB7kfRTVsAMs/aAJM58dzIFN /es/languages/python.js
sha384-ND/UH2UkaeWiej5v/oJspfKDz9BGUaVpoDcz4cof0jaiv/mCigjvy7RQ7e+3S6bg /es/languages/python.min.js
sha384-ckZPeKyE8cW29gT8AxdZNWMC96H8wZCpBzPVkyvuqsGIDvYIzEyxJcckwbv/afrk /es/languages/vim.js
sha384-8kEj1LOKOKcz1ifO10aWlws8zNCnrxWFhHS5zWENNU+dOB/z0X/X31StZHBTQ64Z /es/languages/vim.min.js
sha384-MX3xn8TktkjONV3aWF6Qn6WZyq2Lh/98p0v7D0qEoJ4WLdYjoAyXF/L/80q3qaEc /es/languages/yaml.js
sha384-4IiaMbQ0LBiRJYBGoAXsN+dV9qu/cGLES6IuVowdeCu/FAMY5/MQfD/bHXoL2YBb /es/languages/yaml.min.js
sha384-TNCGFff/wyeX7aiXqfUiRNchsGQ+o1Xy+30DjlGo3zX9i6sIgRdk1VEFMP5MRsFy /languages/applescript.js
sha384-DXh21OyhY78ycqaPwsochxlyc+9KtEG+v6BZxyDRuXWvPXyNvXi2wQKfdaZKlEyg /languages/applescript.min.js
sha384-VZxKf0mjKYDwZIgrW+InqDfJ0YwYUFEMw/4YmpV1oKtVXFVmVq/Ga1vgq6zKTUqS /languages/c.js
sha384-mWenE7UXKnmYRcJ3mh+Os3iZ43BmFf9x3AZMM6gi/2sT6vxouPWspbTdREwWDO3w /languages/c.min.js
sha384-J4Ge+xXjXgzbK2FP+OyzIGHLfKU/RR0+cH4JJCaczeLETtVIvJdvqfikWlDuQ66e /languages/cpp.js
sha384-LMyrRAiUz6we2SGvYrwDd4TJoJZ+m/5c+4n4E64KVkfWFcZdlrs4Wabr0crMesyy /languages/cpp.min.js
sha384-r9czyL17/ovexTOK33dRiTbHrtaMDzpUXW4iRpetdu1OhhckHXiFzpgZyni2t1PM /languages/css.js
sha384-HpHXnyEqHVbcY+nua3h7/ajfIrakWJxA3fmIZ9X9kbY45N6V+DPfMtfnLBeYEdCx /languages/css.min.js
sha384-d6WNn2kPYgdezhgRmGehSkGVKwbg+ImJrGTA43yYg8VsBqYW5TakSDi/jbVjzqfD /languages/diff.js
sha384-yE0kUv4eZRBzwnxh0XmeqImGvOLywSpOZq2m0IH40+vBtkjS716NYEZyoacZVEra /languages/diff.min.js
sha384-BBTUoNxAh4TWINjb22cp1mRwwVdcPyF6zzXZ/1EvQ28ls8EIGhlCKeLav689vLdl /languages/dockerfile.js
sha384-H3wUmCndJNBOuIIzcLSr2zLLZYs8PYuw6qKyENk7THEnYQJvOMDBu42P9XsJSRKw /languages/dockerfile.min.js
sha384-g/lhU6FXH73RQL4eFwkPk4CuudGpbHg6cyVZCRpXft3EKCrcQTToBVEDRStjYWQb /languages/http.js
sha384-wt2eEhJoUmjz8wmTq0k9WvI19Pumi9/h7B87i0wc7QMYwnCJ0dcuyfcYo/ui1M6t /languages/http.min.js
sha384-JSUMPR+WT0h/7NlqXi1Al9bVlNT31AeZNpAHttuzu+r02AmxePeqvsZkKqYZf06n /languages/ini.js
sha384-QrHbXsWtJOiJjnLPKgutUfoIrj34yz0+JKPw4CFIDImvaTDQ/wxYyEz/zB3639vM /languages/ini.min.js
sha384-vJxw3XlwaqOQr8IlRPVIBO6DMML5W978fR21/GRI5PAF7yYi2WstLYNG1lXk6j9u /languages/javascript.js
sha384-44q2s9jxk8W5N9gAB0yn7UYLi9E2oVw8eHyaTZLkDS3WuZM/AttkAiVj6JoZuGS4 /languages/javascript.min.js
sha384-dq9sY7BcOdU/6YaN+YmFuWFG8MY2WYJG2w3RlDRfaVvjdHchE07Ss7ILfcZ56nUM /languages/json.js
sha384-RbRhXcXx5VHUdUaC5R0oV+XBXA5GhkaVCUzK8xN19K3FmtWSHyGVgulK92XnhBsI /languages/json.min.js
sha384-0DF4M/uGwA0TYtI4/4/Nxlz/Z6TObHvf/Uhz39xsvP8TkITbNVOVhbxyOXgyUn2V /languages/latex.js
sha384-0ZgcpgIDZoDPMdyG1FHnl/MByMKt+W52UltboQpuA52+f4pniKOMFXfIfe4K4Byc /languages/latex.min.js
sha384-LmfE+sO0d5qZL2Ka0DIrgJ/5U1plo4uFFAmgjcMxrQO+RkeWVYWuaphHAdrY9g7V /languages/makefile.js
sha384-NIrob3StFQyD/nlOsXVCeRsJ0N2SvFEDjFtYS393wbD3CY1eT+2kwT4RL7tpMMhs /languages/makefile.min.js
sha384-U+zIQPoVdPCO0o4poik2hYNbHtNm+L5OojDTulgIeEZTNz+LooLAm72d66mNjwKD /languages/markdown.js
sha384-mCUujHHbWJEjcupTTfWOk9YR3YCYNHaA578+TTXUd4LPi7fGNuMQbysbl1pmcIGd /languages/markdown.min.js
sha384-zdZio5RcGiKQJCpe/1IXujPle3bIY8sbmvCabSU5G5GzWAzZtoRZfg9QAQXCL08q /languages/python.js
sha384-IP4vv4Aoh9Lyg8QyzVkAmn2JGoDCpgVHzVSrD3Z+rVyn7+s4wx4pRjv+go3TEwfj /languages/python.min.js
sha384-eq5Hd6gkTe5WGbF4XH+7WuiNnuq2zbdo/CV5idmTs5HIdlT6nsfGAJeb2aBqsRO6 /languages/vim.js
sha384-WcP1nsZR09ttNCYSUJGb4LmXw+/kA1O2iyojERHIrTB7Ou0ONLTsIkFOnFF2Umkj /languages/vim.min.js
sha384-tB5cwwsX4Ddp7P4d+ZInDb3nt4ihEEglHXoQ18eVLlT7soEn7bfGfABWKIn1l+H2 /languages/yaml.js
sha384-WC56y8OaFPt5Kj2HX6JAumxUYEjQmBDcSTJy2pn/N8g7dg1hKjeNVrJYoxlpeVmz /languages/yaml.min.js
sha384-O1L+jibjACl+uS/9+jhgtebEejJWbzUqtyKpF0qZftSf3358eyLbfZPgiTJBN7Qe /highlight.js
sha384-nU0Kjnl7YJmshFGYy4pyRSOwolAx9gxiRtgqJwYLwB7Jpk8Xm912ZYXfliQmtcfV /highlight.min.js
```

