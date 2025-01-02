
// #[allow(dead_code)]
// pub fn gen_acts() -> Vec<activity::Act> {
//     let data = r#"
//         [
//             {"user": "Tuan Anh", "paid": 0},
//             {"user": "Truong", "paid": 500},
//             {"user": "Dat beo", "paid": 1300},
//             {"user": "Trung", "paid": 200},
//             {"user": "Hay", "paid": 8000},
//             {"user": "Dung", "paid": 0},
//             {"user": "Tu", "paid": 5000},
//             {"user": "Baxom", "paid": 0}
//         ]"#;
//     let datas: Vec<activity::Act> = serde_json::from_str(data).unwrap();
//     datas
// }

#[cfg(test)]
mod tests {
    #[test]
    fn test_main() {
        // use crate::test::gen_acts;
        // use crate::vkl;
        // let data = gen_acts();
        // let payments = vkl(&data, None);
        // println!("{:#?}", payments);
    }

    #[test]
    fn test_divide() {
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        panic!("go")
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        panic!("Divide result is zero")
    }
}
