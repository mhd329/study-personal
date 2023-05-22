const scaleName = {
    c: "섭씨",
    f: "화씨",
}

// 이 컴포넌트는 Calculator 컴포넌트의 하위 컴포넌트로써 섭씨, 화씨 두 가지 버전으로 사용될 수 있다.
function TemperatureInput(props) {
    const handleChange = (event) => {
        // 어떤 온도가 입력되었을 때 그것을 감지하고 state에 set함
        // setState 해주는 함수는 props에 들어있다.
        // 각각의 섭씨, 화씨 단위의 하위 컴포넌트는 state로 주어진 temperature를 scale에 맞게 등록함
        props.onTemperatureChange(event.target.value);
    };

    return (
        <fieldset>
            <legend>
                온도를 입력해주세요(단위: {scaleName[props.scale]})
            </legend>
            {/* input태그 내부의 값이 변하면 handleChange도 변함(handleChange에서는 event를 감지) */}
            <input value={props.temperature} onChange={handleChange} />
        </fieldset>
    );
}

export default TemperatureInput;