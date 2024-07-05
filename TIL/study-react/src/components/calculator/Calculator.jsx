import React, { useState } from "react";
import TemperatureInput from "./TemperatureInput";

// 일반 함수
function toCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
    return (celsius * 9) / 5 + 32;
}

function tryConvert(temperature, convert) {
    const input = parseFloat(temperature);
    if (Number.isNaN(input)) {
        return '';
    };
    const output = convert(input);
    const rounded = Math.round(output * 1000) / 1000;
    return rounded.toString();
}

// 컴포넌트
function BoilingVerdict(props) {
    if (props.celsius >= 100) {
        return <p>물이 끓습니다.</p>;
    }
    else if (props.celsius <= 0) {
        return <p>물이 얼었습니다.</p>;
    };
    return <p>물이 끓지 않습니다.</p>;
}

function Calculator(props) {
    const [temperature, setTemperature] = useState("");
    const [scale, setScale] = useState("c");

    // 섭씨
    const handleCelsiusChange = (temperature) => {
        setTemperature(temperature);
        setScale("c");
    };

    // 화씨
    const handleFahrenheitChange = (temperature) => {
        setTemperature(temperature);
        setScale("f");
    };

    const celsiusTemperature = scale === "f" ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheitTemperature = scale === "c" ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
        <div>
            <TemperatureInput scale="c" temperature={celsiusTemperature} onTemperatureChange={handleCelsiusChange} />
            <TemperatureInput scale="f" temperature={fahrenheitTemperature} onTemperatureChange={handleFahrenheitChange} />
            <BoilingVerdict celsius={parseFloat(celsiusTemperature)} />
        </div>
    );
}
/*
코드 전개 :
0. scale이 c와 f인 TemperatureInput 컴포넌트 두 개가 렌더링되고 temperature는 빈 값, onTemperatureChange는 현재 변화가 없기 때문에 작동하지 않음
1. 섭씨 온도의 input에 온도가 입력됨
2. scale이 c인 컴포넌트에서 onChange 속성으로 인해 값의 변화가 감지된다.
정확히는 onChange 속성에 의해 handleChange 함수가 input태그의 값 변화를 실시간으로 참조하고 있고,
handleChange 함수는 어떤 event가 발생할 경우 onTemperatureChange를 실행하게끔 만들어져 있다.
3. 감지된 값은 섭씨, 화씨 온도로 설정되고 scale도 단위에 맞게 설정된다.
즉, onChange, handleChange > onTemperatureChange > handleCelsiusChange > setTemperature(temperature), setScale("c")
4. 예를 들어 섭씨 단위로 입력되고 설정된 온도는 화씨로도 변경해서 보여줘야 되므로,
fahrenheitTemperature의 조건식에 의해 tryConvert함수가 작동되어 화씨 변수에도 저장된다.
5. 그리고 섭씨 단위로 입력되었으므로 scale이 f인 TemperatureInput 컴포넌트의 input태그에는 변화가 없고 handleFahrenheitChange도 작동하지 않았다.
celsiusTemperature는 조건식에 의해 그대로 간다.
6. 각각의 컴포넌트에 temperature가 재반영되어 리턴(렌더링)된다.
7. 이제 섭씨, 화씨로 입력하면 변환된 온도가 계산되어 실시간으로 반영되는 것처럼 보이게 된다.
*/
export default Calculator;