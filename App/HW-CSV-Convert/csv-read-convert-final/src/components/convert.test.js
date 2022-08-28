/* Code that tests data conversions


Ana Paula Katsuda - A01025303
Regina Rodriguez - A01284329
Salvador Federico Milanes - A01029956 */


// Importing the jest testing library
import '@testing-library/jest-dom'
import {changeGrade, changeDate, noSurname, format_line} from './convert'

// Many unit tests for functions
describe('Individual functions', () => {
    // Test grade conversion
    test('grade conversion', () => {
      expect(changeGrade(98)).toBe('A+');
      expect(changeGrade(95)).toBe('A');
      expect(changeGrade(91)).toBe('A-');
      expect(changeGrade(89)).toBe('B+');
      expect(changeGrade(85)).toBe('B');
      expect(changeGrade(81)).toBe('B-');
      expect(changeGrade(79)).toBe('C+');
      expect(changeGrade(75)).toBe('C');
      expect(changeGrade(71)).toBe('C-');
      expect(changeGrade(68)).toBe('D+');
      expect(changeGrade(66)).toBe('D');

    });
    // Test date conversion
    test('date conversion', () => {
      expect(changeDate('24/06/2021')).toBe('06/24/2021');
      expect(changeDate('18/12/2021')).toBe('12/18/2021');
      expect(changeDate('23/06/2021')).toBe('06/23/2021');
    });
    // Test remove surname
    test('remove surname', () => {
      expect(noSurname('Regina Rodriguez Sanchez')).toBe('Regina Rodriguez');
      expect(noSurname('Gilberto Echeverria Furio')).toBe('Gilberto Echeverria');
      expect(noSurname('Salvador Milanes Braniff')).toBe('Salvador Milanes');
    });
  
  });
  
  // Test format line
  describe('Complete line', () => {
    test('convert line', () => {
      let line = [];
      let result = [];
      line = ['1', 'Regina Rodriguez Sanchez', 'A01284329', '24/06/2021', '93'];
      result = ['1', 'Regina Rodriguez', 'A01284329@tec.mx', '06/24/2021', 'A'];
      expect(format_line(line)).toStrictEqual(result);
      line = ['2', 'Gilberto Echeverria Furio', 'a09876543', '15/12/2022', '85'];
      result = ['2', 'Gilberto Echeverria', 'a09876543@tec.mx', '12/15/2022', 'B'];
      expect(format_line(line)).toStrictEqual(result);
      line = ['12', 'Salvador Milanes Braniff', 'A01029956', '07/03/2021', '75'];
      result = ['12', 'Salvador Milanes', 'A01029956@tec.mx', '03/07/2021', 'C'];
      expect(format_line(line)).toStrictEqual(result);
    });
  });