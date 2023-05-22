import React from "react";

const students = [
    {
        id: 1,
        name: "Inje",
    },
    {
        id: 2,
        name: "Steve",
    },
    {
        id: 3,
        name: "Bill",
    },
    {
        id: 4,
        name: "Jeff",
    },
];

function AttendanceBook(props) {
    return (
        <ul>
            {/* index를 key로 쓰기 위해서는 아래와 같이 map의 매개변수로 index가 추가로 들어가야 한다. */}
            {/* {students.map((student, index) => */}
            {students.map((student) =>
                // <li key={index}>{student.name}</li>
                // <li key={student.id}>{student.name}</li>
                <li key={`student-id-${student.id}`}>{student.name}</li>
            )}
        </ul>
    );
}

export default AttendanceBook;