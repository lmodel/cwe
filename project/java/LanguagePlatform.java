package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A programming language or language class applicable to a weakness with associated prevalence (Language element in ApplicablePlatformsType).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LanguagePlatform  {

  private String name;
  private String class;
  private String prevalence;

}